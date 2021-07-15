n = int(input())
b = [n]
a = list(map(int,input().split()))
while n != 1:
    b.append(a[n-2])
    n = a[n-2]
if b[len(b)-1] != 1:
    b.append(1)
b = reversed(b)
print(*b , end = ' ')
