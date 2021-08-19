(v1, v2) = [int(next_token) for next_token in input().split()]
(t, d) = [int(next_token) for next_token in input().split()]
ans = v1 + v2
(v1, v2) = (min(v1, v2), max(v1, v2))
t -= 2
while t > 0:
    if v2 - v1 > d:
        v1 += d
        ans += v1
        t -= 1
        continue
    v1 += d
    (v1, v2) = (v2, v1)
    ans += v2
    t -= 1
print(ans)
