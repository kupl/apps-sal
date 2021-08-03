n = int(input())
temp = 0
c = 0
a = input().split()
for i in range(0, n):
    if(temp - int(a[i]) > 0):
        c = i + 1
    temp = int(a[i])
if(c != 0):
    print(c - 1)
else:
    print(0)
