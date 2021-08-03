a, b = map(int, input().split())
ans = b
if a <= 5:
    ans = 0
elif a <= 12:
    ans //= 2
print(ans)
