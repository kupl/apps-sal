n = int(input())
a = [list(input()) for _ in range(n)]
for q in range(n):
    for q1 in range(n):
        if a[q][q1] == '.':
            if q + 2 < n and 0 < q1 and q1 + 1 < n:
                if a[q + 1][q1 - 1] == a[q + 1][q1] == a[q + 1][q1 + 1] == a[q + 2][q1] == '.':
                    a[q][q1] = a[q + 1][q1 - 1] = a[q + 1][q1] = a[q + 1][q1 + 1] = a[q + 2][q1] = '#'
                    continue
            print('NO')
            return
print('YES')
