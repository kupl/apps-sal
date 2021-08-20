n = int(input())
ans = 0
if n == 2 or n == 3:
    print(0)
else:
    i = 2
    while i <= n:
        j = 2
        while j * i <= n:
            ans += j * 4
            j += 1
        i += 1
    print(ans)
