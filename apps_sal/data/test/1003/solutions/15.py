a = [int(i) for i in input().split()]
n = a[0]
m = a[1]
s = 0
while n >= m:
    s += m
    n = n - m + 1
s += n
print(s)
