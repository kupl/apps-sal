a,b,c = map(int, input().split())
x = 0
while a * x <= c:
    if (c - a * x) % b == 0: 
        print('Yes')
        return
    x+=1
print('No')
