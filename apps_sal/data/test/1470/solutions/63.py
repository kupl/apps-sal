x = int(input())
ans = 0
if x <= 6:
    ans = 1
elif x <= 11:
    ans = 2
else:
    ans = (x // 11) * 2
    if 1 <= x % 11 <= 6:
        ans += 1
    elif x % 11 >= 7:
        ans += 2
print(ans)
