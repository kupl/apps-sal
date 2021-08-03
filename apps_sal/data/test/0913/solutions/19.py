from math import ceil
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count1 = 0
count2 = 0
for i in range(n):
    if(a[i] == 1 and b[i] == 0):
        count1 += 1
    elif(a[i] == 0 and b[i] == 1):
        count2 += 1
if(count1 == 0):
    print(-1)
else:
    if(count2 % count1 == 0):
        print(1 + count2 // count1)
    else:
        print(ceil(count2 / count1))
