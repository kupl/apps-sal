a, b = list(map(int, input().split()))
ans = a + b
if a + b >= 10:
    ans = 'error'
print(ans)
