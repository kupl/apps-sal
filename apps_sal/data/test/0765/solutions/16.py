T, S, q = list(map(int, input().split()))
ans = 1
p = 0
while True:
    S = S + (q - 1)
    p += q
    if S >= T:
        break
    if p >= S:
        p = 0
        ans += 1

print(ans)
