s = input()
k = int(input())
p = 10 ** 9 + 7
n = len(s)
amodp = (pow(2, k * n, p) - 1) % p
b1modp = pow(2 ** n - 1, p - 2, p)
MOD = amodp * b1modp % p
ans = 0
for i in range(len(s)):
    if s[i] == '5' or s[i] == '0':
        ans += pow(2, i, 10 ** 9 + 7)
Ans = 0
Ans += ans * MOD
Ans %= p
print(Ans)
