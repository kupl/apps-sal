t = int(input())
while t > 0:
    t -= 1
    n, p = list(map(int, input().split()))
    num = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            num += 1
            if num <= 2*n + p:
                print(i,j)

