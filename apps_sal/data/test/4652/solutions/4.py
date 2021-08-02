n = int(input())
for x in range(n):
    t = int(input())
    r = list(map(int, input().split()))
    r = r + r
    l1 = [x for x in range(1, t + 1)]
    l2 = l1[::-1]
    bo = 0
    for i in range(t):
        if(r[i:i + t] == l1):
            bo = 1
        if(r[i:i + t] == l2):
            bo = 1
    if(bo == 1):
        print("YES")
    else:
        print("NO")
