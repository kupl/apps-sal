n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

w = [[0 for i in range(2)] for i in range(n)]

w[0][1] = c
for i in range(1, n):
    w[i][0] = min(w[i - 1][0] + a[i - 1],
                  w[i - 1][1] + b[i - 1])
    w[i][1] = min(w[i - 1][1] + b[i - 1],
                  w[i][0] + c)

for i in range(n):
    print(min(w[i]), end=' ', flush=False)
print()
