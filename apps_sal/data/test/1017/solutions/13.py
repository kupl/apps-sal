n = int(input())
ans = 0
if n % 3 == 0:
    ans += (n // 3) * 2
elif n % 3 == 1:
    ans += (n // 3) * 2 + 1
elif n % 3 == 2:
    ans += (n // 3) * 2 + 1
print(ans)
