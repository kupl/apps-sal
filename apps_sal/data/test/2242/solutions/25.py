s = input()[::-1]
n = len(s)
p = 2019
S = [0 for i in range(n + 1)]
ans = [0] * p
x10 = 1
for (j, i) in enumerate(s):
    S[j + 1] = (S[j] + x10 * int(i)) % p
    x10 *= 10
    x10 %= p
    ans[S[j + 1]] += 1
cnt = ans[0]
for a in ans:
    cnt += a * (a - 1) // 2
print(cnt)
