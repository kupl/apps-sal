a,b = map(int,input().split())
#lis = list(map(int,input().split()))
count = 0
if a>b:
    count += a
    a -= 1
else:
    count += b
    b -= 1
if a>b:
    count += a
    a -= 1
else:
    count += b
    b -= 1
print(count)
