A, B, C, D = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    if C <= i <= D:
        ans += 1
if ans > 0:
    ans -= 1
print(ans)
