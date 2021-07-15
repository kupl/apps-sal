t = int(input())

while t > 0:
    [n, p] = map(int, input().split(' '))
    count = int(0)
    for i in range(n):
        j = i+2
        while j <= n:
            count = count+1
            print(str(i+1)+' '+str(j))
            if count == 2*n+p:
                break
            j = j + 1
        if j <= n:
            break
    t = t-1
