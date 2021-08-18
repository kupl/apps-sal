S, C = list(map(int, input().split()))
ans = 0

if S * 2 <= C:
    C = C - S * 2
    ans += S
    ans += C // 4
else:
    ans += C // 2

print((int(ans)))
