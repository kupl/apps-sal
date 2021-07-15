n = int(input())
a = list(map(int, input().split()))
o = []
for i in range(2 * n):
    o.append(a[i % n])
m = 0
t = 0
for i in range(2 * n):
    if o[i] == 1:
        t += 1
    else:
        if t > m:
            m = t
        t = 0
print(m)
