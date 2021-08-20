n = int(input())
a = [int(x) for x in input().split()]
m = 1
t = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        t += 1
    else:
        t = 1
    if t > m:
        m = t
print(m)
