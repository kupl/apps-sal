n, L, a = list(map(int, input().split()))
ans = 0
lastt = 0
for i in range(n):
    t, l = list(map(int, input().split()))
    ans += (t - lastt) // a
    lastt = t + l
ans += (L - lastt) // a
print(ans)
