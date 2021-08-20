N = int(input())
res = {}
ans = 0
i = 2
for i in range(2, int(N ** (1 / 2)) + 1):
    while N % i == 0:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
        N /= i
if N != 1:
    res[N] = 1
for i in res:
    b = 1
    s = res[i]
    while b <= s:
        ans += 1
        s -= b
        b += 1
print(ans)
