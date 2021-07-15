n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()
b.sort()
count = 0
while a and b:
    if abs(a[0]-b[0]) <= 1:
        count += 1
        a.pop(0)
        b.pop(0)
    elif a[0] < b[0]:
        a.pop(0)
    else:
        b.pop(0)
print(count)       

