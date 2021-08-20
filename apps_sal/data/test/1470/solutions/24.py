x = int(input())
ans = x // 11 * 2
if 0 < x % 11 < 7:
    ans += 1
elif x % 11 >= 7:
    ans += 2
print(ans)
