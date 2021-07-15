x = int(input())
ans = 0
ans += x // 5
if x % 5 != 0:
    ans += 1
print(ans)
