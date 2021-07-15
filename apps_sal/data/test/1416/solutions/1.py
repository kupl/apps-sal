n, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
t = min(a[0]*2, a[len(a) // 2])
print(min(w, (t * len(a) // 2) + (t/2)*(len(a) // 2)))

