n = int(input())
if n % 2 != 0:
    print(0)
else:
    ans = 0
    dum = 5
    while n > dum:
        ans += (n // dum) // 2
        dum = dum * 5
    print(ans)
