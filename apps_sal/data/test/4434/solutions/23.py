t = int(input())
while t:
    n = int(input())
    ans = 0
    if n==1: print(0)
    else:
        for i in range(1, n//2 + 1):
            ans += 8*i*i
        print(ans)
    t -= 1
