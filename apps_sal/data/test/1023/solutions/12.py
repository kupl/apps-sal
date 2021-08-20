t = list(map(int, input().split(' ')))
n = t[0]
m = t[1]
ta = t[2]
tb = t[3]
k = t[4]
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
b1 = []
j = 0
q = 0
for i in range(n):
    a[i] = a[i] + ta
    while j < m:
        if a[i] <= b[j]:
            q += 1
            b1.append(b[j])
            j += 1
            break
        j += 1
if q <= k:
    print(-1)
else:
    print(b1[k] + tb)
