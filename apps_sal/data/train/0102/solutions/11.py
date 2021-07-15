t = int(input())
for kkk in range(t):
    n = int(input())
    ans = 0
    nn = len(str(n))
    for i in range(1, 10):
        ans += (nn - (1 if int(str(i) * nn) > n else 0))
    print(ans)

