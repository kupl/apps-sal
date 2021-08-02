t = int(input())
for _ in range(t):
    n = int(input())
    c, d = 0, 0
    bo = 0
    for i in range(n):
        a, b = list(map(int, input().split()))
        if(a < c or b < d):
            bo = 1
        elif(a - c < b - d):
            bo = 1
        c, d = a, b
    if(bo):
        print("NO")
    else:
        print("YES")
