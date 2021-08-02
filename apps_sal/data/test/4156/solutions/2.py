n, w = list(map(int, input().split()))
v = list(map(int, input().split()))

mini, maxi = 0, 0
s = 0
for i in range(n):
    s += v[i]
    mini = min(mini, s)
    maxi = max(maxi, s)

res = max(0, w - (maxi - mini) + 1)
print(res)
