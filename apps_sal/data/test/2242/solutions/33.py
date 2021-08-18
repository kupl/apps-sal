s = list(input())
n = len(s)
ans = 0
s.reverse()
x = 1
tot = 0
count = [0] * 2019
for i in range(n):
    count[tot] += 1
    tot += int(s[i]) * x
    tot %= 2019
    ans += count[tot]
    x = x * 10 % 2019
print(ans)
