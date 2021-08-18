n = int(input())
a = list(map(int, input().split()))
lim = (10 ** 9) + 7
ans = 0
temp = a[-1]
for i in range(2, n + 1):
    ans += a[-i] * temp
    temp += a[-i]

print(ans % lim)
