x = int(input())

ans = x // 11 * 2
x %= 11
if x == 0:
    pass
elif x  > 6:
    ans += 2
else:
    ans += 1
print(ans)
