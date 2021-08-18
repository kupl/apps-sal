
n = int(input())
a = [int(x) for x in input().split()]
r = m = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        r += 1
    else:
        r = 1
    m = r if r > m else m
print(m)
