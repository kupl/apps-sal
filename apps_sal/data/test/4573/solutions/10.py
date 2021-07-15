n = int(input())
x = list(map(int,input().split()))
lis = sorted(x)
key1 = lis[n//2-1]
key2 = lis[n//2]
for i in x:
    if i > key1:
        print(key1)
    else:
        print(key2)

