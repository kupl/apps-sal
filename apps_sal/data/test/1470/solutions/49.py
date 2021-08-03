x = int(input())
ans = (x // 11) * 2
x = x % 11
if 1 <= x <= 6:
    ans += 1
if 7 <= x <= 11:
    ans += 2
print(ans)
