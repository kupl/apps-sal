(n, m) = map(int, input().split())
ta = input()
tb = input()
count = 0
ans = 0
r = n - m
for i in range(m):
    if tb[i] == '1':
        count += 1
    if i + r >= 0:
        if ta[i + r] == '1':
            ans = (ans + pow(2, m - i - 1, 998244353) * count) % 998244353
print(ans)
