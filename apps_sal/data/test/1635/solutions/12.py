n = int(input())
a = list(map(int, input().split(' ')))
d = {}
for i in range(n):
    d[a[i]] = i
min = n
min_k = -1
for k in d:
    if d[k] < min:
        min = d[k]
        min_k = k
print(min_k)
