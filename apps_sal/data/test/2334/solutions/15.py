import math
n = int(input())
ch = input().split()
a = list()
for i in range(n):
    a.append(int(ch[i]))
ch = input().split()
max1 = int(ch[0])
fee = int(ch[1])
a.sort(reverse=True)
result = 0
for i in range(n):
    if (a[i] <= max1):
        break
    k = a[i] + fee
    result += (math.ceil(k / (fee + max1))) - 1
print(result * fee)
