x = int(input())
a = list(map(int, input().strip().split()))
y = []
c = 0
f1 = 1
f2 = 1
l = 0
r = x - 1
op = []
while(f1 or f2):
    if(l > r):
        break
    if(a[l] < c):
        f1 = 0
    if(a[r] < c):
        f2 = 0
    if(f1 and f2):
        if(a[l] <= a[r]):
            c = a[l]
            l = l + 1
            op.append('L')
        else:
            c = a[r]
            r = r - 1
            op.append('R')
    elif(f1):
        c = a[l]
        l = l + 1
        op.append('L')
    elif(f2):
        c = a[r]
        r = r - 1
        op.append('R')
print(len(op))
print("".join(op))
