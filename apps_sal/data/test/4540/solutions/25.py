n = int(input())
a = [0] + list(map(int, input().split())) + [0]

res = [0] * (n + 1)
for i in range(n + 1):
    res[i] = abs(a[i] - a[i + 1])

t = sum(res)
for i in range(1, n + 1):
    ans = t - (res[i - 1] + res[i]) + abs(a[i - 1] - a[i + 1])
    print(ans)
