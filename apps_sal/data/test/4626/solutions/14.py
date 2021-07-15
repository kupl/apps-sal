q = int(input())
for numbers in range(q):
    a,b,c = list(map(int,input().split()))
    x = max(a,b,c)
    y = min(a,b,c)
    if x - y <=2 :
        print(0)
    else:
        print(2*(x-y-2))
        


