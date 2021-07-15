t = int(input())
while t > 0 : 
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 1
    for i in range(n) :
        if a[i] <= i + 1 :
            ans = i + 2
    print(ans)
