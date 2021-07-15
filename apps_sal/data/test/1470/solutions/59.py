x = int(input())
ans = x // 11 * 2
rem = x % 11
if rem != 0 and rem < 7:
    ans += 1
elif rem != 0 and rem > 6:
    ans += 2
print(ans)
