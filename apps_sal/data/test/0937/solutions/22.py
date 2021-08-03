n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sumx = 0
sum1 = 0
s = 0
for i in range(n):
    if(b[i] == 1):
        sum1 += a[i]
for i in range(k):
    if(b[i] == 0):
        sumx += a[i]
s = sumx + sum1
for i in range(k, n):
    if(b[i - k] == 0):
        sumx -= a[i - k]
    if(b[i] == 0):
        sumx += a[i]
    if(sumx + sum1 > s):
        s = sumx + sum1
print(s)
