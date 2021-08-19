a = [list('+------------------------+'), list('|#.#.#.#.#.#.#.#.#.#.#.|D|)'), list('|#.#.#.#.#.#.#.#.#.#.#.|.|'), list('|#.......................|'), list('|#.#.#.#.#.#.#.#.#.#.#.|.|)'), list('+------------------------+')]
a = list(a)
k = int(input())
if k < 4:
    for i in range(k):
        a[1 + i][1] = 'O'
else:
    for i in range(4):
        a[1 + i][1] = 'O'
    k -= 4
    for i in range(k):
        r = i % 3
        if r == 0:
            a[1][i // 3 * 2 + 3] = 'O'
        elif r == 1:
            a[2][i // 3 * 2 + 3] = 'O'
        elif r == 2:
            a[4][i // 3 * 2 + 3] = 'O'
for i in a:
    print(''.join(i))
