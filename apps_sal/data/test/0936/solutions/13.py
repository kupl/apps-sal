n = int(input())
a = [0] * 1000001
m = 0
l = list(map(int, input().split()))
for i in range(n):
    a[l[i]] += 1
    if a[l[i]] > m:
        m = a[l[i]]
        j = l[i]
print(j)
