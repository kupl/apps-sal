n, m = list(map(int, input().split()))
ans = [0] * n

for _ in range(m):
    a, b, = list(map(int, input().split()))
    ans[a - 1] += 1
    ans[b - 1] += 1

for i in range(n):
    print((ans[i]))
