a = list(map(int,input().split()))
b = sum(a)
if(b%5 or b == 0):
    print(-1)
else:
    print(int(b/5))

