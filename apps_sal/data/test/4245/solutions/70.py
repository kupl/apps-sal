a,b = map(int,input().split())
if b == 1:
    print(0)
else:
    for i in range(1,100):
        ans = 1 + i * (a - 1)
        if ans >= b:
            print(i)
            break
