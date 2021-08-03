t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    columns = list(map(int, input().split()))
    bag = m
    ok = True
    for i in range(n - 1):
        if columns[i + 1] - columns[i] > k:
            bag -= (columns[i + 1] - columns[i]) - k
            if bag < 0:
                ok = False
                break
        else:
            bag += columns[i] - max(0, columns[i + 1] - k)
    print('YES' if ok else 'NO')
