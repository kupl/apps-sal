n = int(input())

if n % 2 == 1:
    print(0)
    return

ans = 0
n = n // 2
while n > 0:
    n = n // 5
    ans += n

print(ans)
