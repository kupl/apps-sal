n = int(input())
a = []
d = {}
l = 0
k = n
while l < n:
    a.append(input())
    d[a[l]] = False
    l += 1

k = k - 1
while k >= 0:
    if not d[a[k]]:
        print(a[k])
        d[a[k]] = True
    k -= 1
