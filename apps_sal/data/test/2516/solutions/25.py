N, P = map(int, input().split())
S = list(map(int, list(input())))[::-1]
counter = [0] * P
counter[0] = 1
ans = 0
sum = 0
d = 0
r = []
mod = 0

if P != 2 and P != 5:
    mod = 1 % P
    for i in range(N):
        d = S[i] * mod
        sum = (sum + d) % P
        mod = (mod * 10) % P
        counter[sum] += 1
    for k in range(P):
        ans += (counter[k] * (counter[k] - 1)) // 2

if P == 2 or P == 5:
    if P == 2:
        r = [0, 2, 4, 6, 8]
    if P == 5:
        r = [0, 5]
    for j in range(N):
        if S[j] in r:
            ans += N - j

print(ans)
