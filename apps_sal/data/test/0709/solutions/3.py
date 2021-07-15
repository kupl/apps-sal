x = int(input())

ans = 0
while x > 0:
    ans += x % 2
    x //= 2
print(ans)

