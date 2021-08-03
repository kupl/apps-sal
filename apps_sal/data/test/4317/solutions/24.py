a, b = map(int, input().split())

ans = a + b
if (a - b) > ans:
    ans = a - b
if (a * b) > ans:
    ans = a * b

print(ans)
