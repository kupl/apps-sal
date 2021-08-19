(a, b) = map(int, input().split())
ans = 0
if a >= 13:
    ans = b
elif a >= 6:
    ans = b // 2
else:
    ans = 0
print(ans)
