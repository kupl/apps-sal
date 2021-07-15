n, m = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
a.append(m)
a.insert(0, 0)
n += 2
diff = [0] * (n - 1)
d = n - 2
for i in range(n - 1, 0, -1):
    diff[d] = a[i] - a[i - 1]
    if (i < n - 2):
        diff[d] += diff[d + 2]
    d -= 1
ontime = diff[0] 
for d in range(n - 1):
    
    if (d % 2 == 0):
        prevontime = diff[0] - diff[d]
        afterofftime = 0
        if (d < n - 2):
            afterofftime += diff[d + 1]
        ontime = max(ontime,  prevontime + afterofftime + a[d + 1] - a[d] - 1)
    else:
        if (a[d] + 1 == a[d + 1]):
            continue
        prevontime = diff[0]
        if (d < n - 2):
            prevontime -= diff[d + 1]
        afterofftime = 0
        if (d < n - 3):
            afterofftime += diff[d + 2]
        ontime = max(ontime, prevontime + afterofftime + 1)
print(ontime)
