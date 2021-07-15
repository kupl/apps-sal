t = int(input())
for i in range(t):
    a0, a1, a2 = map(int , input().split())
    b0, b1, b2 = map(int , input().split())

    ans = 2*min(a2,b1)
    a2 = max(0 , a2 - min(a2,b1))

    if b2 > (a0+a2):
        ans -= (2*(b2 - a0 - a2))
    print(ans)
