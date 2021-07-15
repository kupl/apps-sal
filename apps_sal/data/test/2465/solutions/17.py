tc = int(input())
while tc!=0:
    a = int(input())
    n = 3
    tc-=1
    if a==180:
        print("-1")
        continue
    while True:
        z = 180/n
        if a%z==0 and a/z<=n-2:
            break
        n+=1
    print(n)
