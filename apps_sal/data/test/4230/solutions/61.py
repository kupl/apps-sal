x,n=list(map(int, input().split()))
p=list(map(int, input().split()))
dif=0
for i in range(100):
    if x-i not in p:
        print((x-i))
        break
    elif x+i not in p:
        print((x+i))
        break

