def op(n):
    m = 3
    l = [[1], [2], [4], [3]]

    for _ in range(n - 1):
        for row in l:
            if row == l[2]:
                row.append(row[-1] + 2 * m)
            else:
                row.append(row[-1] + m)
        m = m * 2

    for row in l:
        for elem in row:
            print(elem, end=" ")
        print("\n")


t = int(input())
ns = list(map(int, input().split()))
for n in ns:
    op(n)
