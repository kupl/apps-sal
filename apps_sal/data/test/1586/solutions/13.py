n = int(input())
if n % 2 == 1:
    print(0)

else:
    ans = 0
    while n >= 5:
        ans += (n // 5) // 2
        n //= 5
    print(ans)
