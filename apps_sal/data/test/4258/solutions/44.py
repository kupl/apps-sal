A, B, T = list(map(int, input().split()))

i = 1
ans = 0
while i*A <= T+0.5:
    ans += B
    i += 1

print(ans)

