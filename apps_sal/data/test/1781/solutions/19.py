def main():
    n, k = map(int, input().split())
    lines = list()
    m = [0, 0, 0]
    v = 0
    for i in range(n):
        lines.append(input() + ' ')
        for j in range(12):
            if lines[i][j] == '.':
                c = 0
                if lines[i][j - 1] == 'S':
                    c += 1
                if lines[i][j + 1] == 'S':
                    c += 1
                m[c] += 1
            elif lines[i][j] == 'S':
                if lines[i][j - 1] == 'S' or lines[i][j - 1] == 'P':
                    v += 1
                if lines[i][j + 1] == 'S' or lines[i][j + 1] == 'P':
                    v += 1
    m[0] = min(m[0], k)
    k -= m[0]
    m[1] = min(m[1], k)
    k -= m[1]
    m[2] = min(m[2], k)
    v += m[1] + 2 * m[2]
    print(v)
    for elem in lines:
        for j in range(12):
            if elem[j] == '.':
                c = 0
                if elem[j - 1] == 'S':
                    c += 1
                if elem[j + 1] == 'S':
                    c += 1
                if m[c] > 0:
                    print('x', end='')
                    m[c] -= 1
                else:
                    print('.', end='')
            else:
                print(elem[j], end='')
        print()


main()
