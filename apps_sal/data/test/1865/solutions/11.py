def find_min(i):
    min = 1000000001
    index = 0
    for j in range(i, n):
        if a[j] < min:
            min = a[j]
            index = j
    return index

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

k = 0
ans = ()

for i in range(n):
    m = find_min(i)
    if i != m:
        a[i] = a[i] + a[m]
        a[m] = a[i] - a[m]
        a[i] = a[i] - a[m]
        ans += (i, m)
        k += 1
    
print(k)
for i in range(0, len(ans), 2):
    print(ans[i], ans[i+1])
