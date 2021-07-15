t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        if(a[i] in d):
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    flag = 1
    for i in d:
        if(len(d[i]) >= 3):
            print("YES")
            break
    else:
        for i in d:
            if(len(d[i]) >= 2 and d[i][-1] - d[i][0] >= 2):
                print("YES")
                break
        else:
            print("NO")
