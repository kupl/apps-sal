A, B, C = map(int, input().split())

ans = "NO"
for i in range(1, 1000):
    a = A * i
    if a % B == C:
        ans = "YES"
        break

print(ans)
