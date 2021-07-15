n = int(input())
s = input()
MOD = 998244353
pre = s[0]
num1, num2 = 1, 1
for i in range(1, n):
    if pre != s[i]:
        break
    num1 += 1

sur = s[-1]
for i in range(n - 2, -1, -1):
    if sur != s[i]:
        break
    num2 += 1

num1, num2 = num1 + 1, num2
if pre == sur:
    print(num1 * (num2 + 1) % MOD)
else:
    print((num1 + num2) % MOD)
