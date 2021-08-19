s = list(input())
# s = list(str(10**200000))
n = len(s)
ans = 0
s.reverse()
# print(s)
x = 1
tot = 0
count = [0] * 2019
for i in range(n):
    count[tot] += 1
    tot += int(s[i]) * x
    # print(tot)
    tot %= 2019
    ans += count[tot]
    x = x * 10 % 2019
print(ans)
