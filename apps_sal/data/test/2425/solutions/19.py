3

q = int(input())
for i in range(q):
    a = int(input())
    ans = 1
    while ans <= a:
        ans *= 2
    if a < ans - 1:
        print(ans - 1)
    else:
        ans = 1
        d = 2
        while d * d <= a:
            if a % d == 0:
                ans = a // d
                break
            d += 1
        print(ans)
