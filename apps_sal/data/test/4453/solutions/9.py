t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    for i in l:
        aa = i
        a = i
        d = 0
        while 1:
            a = l[a - 1]
            d += 1
            if(a == aa):
                break
        print(d, end=" ")
    print()
    t -= 1
