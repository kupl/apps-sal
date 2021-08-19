(a, b, c) = map(int, input().split())
ans = a + b
if a + c < ans:
    ans = a + c
if b + c < ans:
    ans = b + c
print(ans)
