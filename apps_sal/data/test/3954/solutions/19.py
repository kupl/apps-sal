n, k = map(int, input().split())
a = [int(i) for i in input().split()]
best = max(a)
for left in range(n):
    for right in range(left, n):
        inner = a[left:right + 1]
        outer = a[0:left] + a[right + 1:]
        inner.sort()
        outer.sort(reverse=True)
        for i in range(k):
            if i >= len(outer) or i >= len(inner):
                break
            if inner[i] < outer[i]:
                inner[i] = outer[i]
            else:
                break
        best = max(best, sum(inner))
print(best)
