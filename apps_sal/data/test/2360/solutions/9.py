t = int(input())
for y in range(t):
    n = int(input())
    data = []
    tim = 1
    ans = []
    for st in range(n):
        l, r = [int(x) for x in input().split()]
        if(tim <= l):
            tim = l
            ans.append(tim)
            tim +=1
            continue
        if(tim <= r):
            ans.append(tim)
        else:
            ans.append(0)
            continue
        tim+=1

    print(*ans)
    #    data.append([int(x) for x in input().split()])
    


