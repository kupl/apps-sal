n, m = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(n)]
r = 0
for k in range(n):
    for i in range(m):
        if L[k][2 * i + 1] or L[k][2 * i]:
            r += 1
print(r)
