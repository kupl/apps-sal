
A, B, C = map(int, input().split())

ans = "NO"
for i in range(B + 1):
    res = A * i % B
    if res == C:
        ans = "YES"
        break

print(ans)
