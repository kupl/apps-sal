from itertools import accumulate
H, n = list(map(int, input().split()))
D = list(map(int, input().split()))
accD = list(accumulate(D))
d = sum(D)
m = min(accD)
ans = 0
now = H
if H + m <= 0:
    for i in range(n):
        ans += 1
        now += D[i]
        if now <= 0:
            break
elif d >= 0:
    ans = -1
else:
    ans = ((H + m) // (-d)) * n
    now = H + (H + m) // (-d) * d
    while now > 0:
        for i in range(n):
            ans += 1
            now += D[i]
            if now <= 0:
                break
print(ans)
