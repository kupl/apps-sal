N = int(input())

if N%2 == 1:
    print((0))
else:
    ans = 0
    sum = 0
    for i in range(26,0,-1):
        num = N//((5**i)*2)
        ans += i*(num-sum)
        sum = num
    print(ans)

