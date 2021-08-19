MOD = 10 ** 9 + 7
n = int(input())
s = input()
leftQ = [0 for i in range(n)]
rghtQ = [0 for i in range(n)]
leftA = [0 for i in range(n)]
rghtC = [0 for i in range(n)]
for i in range(1, n):
    leftQ[i] = leftQ[i - 1] + (1 if s[i - 1] == '?' else 0)
    leftA[i] = leftA[i - 1] + (1 if s[i - 1] == 'a' else 0)
for i in range(n - 2, -1, -1):
    rghtQ[i] = rghtQ[i + 1] + (1 if s[i + 1] == '?' else 0)
    rghtC[i] = rghtC[i + 1] + (1 if s[i + 1] == 'c' else 0)
ans = 0
for i in range(n):
    if s[i] == 'b' or s[i] == '?':
        ans += leftA[i] * rghtC[i] * pow(3, leftQ[i], MOD) * pow(3, rghtQ[i], MOD)
        if leftQ[i] > 0:
            ans += leftQ[i] * rghtC[i] * pow(3, leftQ[i] - 1, MOD) * pow(3, rghtQ[i], MOD)
        if rghtQ[i] > 0:
            ans += leftA[i] * rghtQ[i] * pow(3, leftQ[i], MOD) * pow(3, rghtQ[i] - 1, MOD)
        if leftQ[i] > 0 and rghtQ[i] > 0:
            ans += leftQ[i] * rghtQ[i] * pow(3, leftQ[i] - 1, MOD) * pow(3, rghtQ[i] - 1, MOD)
        ans %= MOD
print(ans)
