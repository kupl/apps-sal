c = sorted(list(map(int,input().split())))
if c[0] + c[1] >= c[2]//2 :
    print(sum(c)//3)
else :
    print(c[0] + c[1])
