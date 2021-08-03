import itertools


class SolutionImpossible(Exception):
    pass


blocks_cnt, finish, min_sprint, max_jump = [int(x) for x in input().split()]


def read_blocks_coords():
    it = (int(x) for x in input().split())
    return (x for x in it if x < finish)


# TODO: код можно сократить за счет избавления от лишней записи в `_grouper._current_key`
def _grouper(value):
    if _grouper._prev_value is not None:
        # после прыжка мы приземляемся ЗА препятствием, учитываем это
        if value - _grouper._prev_value - 1 <= min_sprint:
            # расстояние между препятствиями слишком мало
            # чтобы между ними приземляться, и затем разогнаться для нового прыжка, считаем их за одно
            _current_key = _grouper._current_key
        else:
            _current_key = id(value)
    else:
        # первое вхождение, ставим данные по умолчанию
        _current_key = id(_grouper)

    _grouper._prev_value = value
    _grouper._current_key = _current_key

    return _current_key


_grouper._prev_value = None
_grouper._current_key = None


def check_chunk(run_from, block=None):
    if block is None:
        return

    next_run_from = block[-1] + 1  # следующая за преградой позиция (точка приземления)
    if next_run_from - block[0] >= max_jump:
        # если преграда слишком длинная, то мы не можем ее пересечь
        raise SolutionImpossible

    if abs(run_from - block[0]) <= min_sprint:
        # нет возможности для разбега
        raise SolutionImpossible


def solve_chunk(run_from, block=None):
    if block is not None:
        run_len = block[0] - run_from - 1  # добегаем ДО преграды
        jump_len = block[-1] - block[0] + 2  # прыгаем ЗА нее
        print((
            "RUN {run_len}\n"
            "JUMP {jump_len}".format(
                run_len=run_len,
                jump_len=jump_len,
            )
        ))

    else:
        run_len = finish - run_from
        if run_len > 0:
            print("RUN {run_len}".format(run_len=run_len))


def main():
    # некоторые препятствия могут находиться так близко, что между ними нет возможности разогнаться
    # считаем такие препятствия за одно
    blocks = (list(g) for k, g in itertools.groupby(sorted(read_blocks_coords()), key=_grouper))

    chunks = []

    run_from = 0
    while True:
        block = next(blocks, None)

        chunk = (run_from, block)
        check_chunk(*chunk)

        chunks.append(chunk)

        if block is None:
            break

        # после прыжка мы приземляемся ЗА препятствием, учитываем это
        run_from = block[-1] + 1

    # print(chunks)

    for chunk in chunks:
        solve_chunk(*chunk)


def __starting_point():
    try:
        main()
    except SolutionImpossible:
        print("IMPOSSIBLE")


__starting_point()
