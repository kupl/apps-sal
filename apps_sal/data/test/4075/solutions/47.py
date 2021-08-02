from itertools import product
n, m = map(int, input().split())
p = 2

iterator = product(range(p), repeat=n)

s = [0 for i in range(m)]
for i in range(m):
    S = list(map(int, input().split()))
    k = S[0]
    s[i] = S[1:]

p = list(map(int, input().split()))

ans = 0
for idxs in iterator:
    tmp1 = 0
    for i in range(m):
        tmp2 = 0
        for j in s[i]:
            tmp2 += idxs[j - 1]
        if tmp2 % 2 == p[i]:
            tmp1 += 1
    if tmp1 == m:
        ans += 1
print(ans)
