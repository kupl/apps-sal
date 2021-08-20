(a, b) = map(int, input().split())
if a <= 5:
    ans = 0
elif 6 <= a <= 12:
    ans = b // 2
else:
    ans = b
print(ans)
