x = int(input())
ans = 2 * (x // 11)
x %= 11
if 0 < x and x < 7:
    ans += 1
elif x != 0:
    ans += 2
print(ans)
