t = int(input())

while t > 0:
    n = int(input())
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if int(str(i) * j) <= n:
                #print(str(i) * j)
                ans += 1
    print(ans)

    t -= 1

