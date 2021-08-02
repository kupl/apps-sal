n, T = list(map(int, input().split()))

t = list(map(int, input().split()))
ans = 0
for i, j in zip(t, t[1:]):
    ans += min(j - i, T)
print((ans + T))
