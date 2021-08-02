n = int(input())
a = [int(input()) - 1 for _ in range(n)]
id = [-1] * n
x = 0
for c in range(1, n + 1):
    if id[x] != -1:
        print(-1)
        return
    id[x] = c
    x = a[x]
    if x == 1:
        print(c)
        return
