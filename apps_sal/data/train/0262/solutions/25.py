
def make_zip(lists):
    i = 0
    maxlength = max(len(l) for l in lists)
    ans = []
    while i < maxlength:
        ans.append([l[i] for l in lists if i < len(l)])
        i += 1
    return ans


def make_order(words, result):
    order = []
    formulas = {}
    for i in range(len(result)):
        for ch in [*(words[i]), result[i]]:
            if ch not in order:
                order.append(ch)
        order.append(f'c{i+1}')
        lhs = words[i]
        rhs = result[i]
        if i > 0:
            lhs.append(f'c{i}')
        excess = f'c{i+1}'
        formulas[excess] = (lhs, rhs, excess)
    return order, formulas


def find_free(repl, ch, nonzero):
    start = 1 if ch in nonzero else 0
    choices = set(range(start, 10))
    for x, y in repl.items():
        if y in choices:
            choices.remove(y)
    yield from choices


def find_value(n, repl, crepl):
    return repl[n] if n in repl else crepl[n]


def find_excess(lhs, rhs, repl, crepl):
    return sum(find_value(x, repl, crepl) for x in lhs) - find_value(rhs, repl, crepl)


def walk_solutions(puzzle, index, repl, crepl):
    (words, result, order, formulas, nonzero) = puzzle

    if index == len(order):
        last_ch = order[-1]
        if crepl[last_ch] != 0:
            return
        yield repl
    else:
        ch = order[index]
        if len(ch) == 1:
            for digit in find_free(repl, ch, nonzero):
                repl[ch] = digit
                yield from walk_solutions(puzzle, index + 1, repl, crepl)
                del repl[ch]
        else:
            formula = formulas[ch]
            (lhs, rhs, _) = formula
            excess = find_excess(lhs, rhs, repl, crepl)
            if excess >= 0 and excess % 10 == 0:
                crepl[ch] = excess // 10
                yield from walk_solutions(puzzle, index + 1, repl, crepl)
                del crepl[ch]


def is_solvable(words, result):
    n = len(words)
    maxword = 10 ** max(len(w) for w in words) - 1
    minresult = 10 ** (len(result) - 1)
    if n * maxword < minresult:
        return False

    if not all(len(w) <= len(result) for w in words):
        return False

    nonzero = {m[0] for m in [*words, result] if len(m) > 1}

    result = [ch for ch in result[::-1]]
    words = make_zip([w[::-1] for w in words])
    while len(words) < len(result):
        words.append([])

    order, formulas = make_order(words, result)

    puzzle = (words, result, order, formulas, nonzero)

    return any(walk_solutions(puzzle, 0, {}, {}))


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        return is_solvable(words, result)
