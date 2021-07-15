n, l, a = map(int, input().split())
prev = 0
num = []
for i in range(n):
    t, x = map(int, input().split())
    num.append(t - prev)
    prev = t + x
num.append(l - prev)
ans = 0
for elem in num:
    ans += elem // a
print(ans)
