s = ['+------------------------+', '|#.#.#.#.#.#.#.#.#.#.#.|D|)', '|#.#.#.#.#.#.#.#.#.#.#.|.|', '|#.......................|', '|#.#.#.#.#.#.#.#.#.#.#.|.|)', '+------------------------+']
k = int(input())
for _ in range(k):
    fnd = False
    for j in range(22):
        if fnd:
            break
        for i in range(6):
            if s[i][j] == '#':
                s[i] = s[i][:j] + 'O' + s[i][j + 1:]
                fnd = True
                break
print('\n'.join(s))
