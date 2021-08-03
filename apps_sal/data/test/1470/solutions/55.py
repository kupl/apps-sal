x = int(input())
ans = x // 11 * 2
rem = x % 11
if rem > 6:
    ans += 2
elif rem > 0:
    ans += 1
print(ans)
