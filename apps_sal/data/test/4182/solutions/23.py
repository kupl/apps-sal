n,m,x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse = True)
b.sort()
bool = False
if a[0] < b[0]:
    for i in range(a[0] + 1,b[0] + 1):
        if x < i and i <= y:
            bool = True
if bool:
    print('No War')
else:
    print('War')
