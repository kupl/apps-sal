k = int(input())
for da in range(k):
    n = int(input())
    cs = [0] * (n+10)
    a = list(map(int,input().split()))
    for i in a:
        cs[i] += 1
    cc = 0
    for i in range(len(cs)-1, 0, -1):
        cc += cs[i]
        if cc >= i:
            print(i)
            break
    

