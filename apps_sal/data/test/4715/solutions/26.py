a, b, c = map(int, input().split())
ans = 1
if b != a:
    ans += 1
if a != c and b != c:
    ans += 1
print(ans)
