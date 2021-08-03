a, b = map(int, input().split())
ans = (a + b) // 2
if a % 2 != b % 2:
    ans = 'IMPOSSIBLE'
print(ans)
