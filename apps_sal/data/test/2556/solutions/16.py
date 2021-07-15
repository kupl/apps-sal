n = int(input())
for i in range(n):
    (c, b) = list(map(int, input().split()))
    a = b // c
    b -= a*c
    ans = 0
    for j in range(c):
        if b == 0:
           ans += a*a
        else:
            ans += (a+1)*(a+1)
            b -= 1
    print(ans)
