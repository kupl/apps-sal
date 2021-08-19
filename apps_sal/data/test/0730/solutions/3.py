bus = [list('+------------------------+'), list('|#.#.#.#.#.#.#.#.#.#.#.|D|)'), list('|#.#.#.#.#.#.#.#.#.#.#.|.|'), list('|#.......................|'), list('|#.#.#.#.#.#.#.#.#.#.#.|.|)'), list('+------------------------+')]
n = int(input())
for i in range(n):
    ok = False
    for r in range(11):
        if ok:
            break
        r_num = 2 * r + 1
        for j in range(1, 5):
            if ok:
                break
            if bus[j][r_num] == '#':
                bus[j][r_num] = 'O'
                ok = True
for s in bus:
    print(''.join(s))
