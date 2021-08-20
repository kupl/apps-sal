(n, k) = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
best = max(A)
for left in range(n):
    for right in range(left, n):
        inner = A[left:right + 1]
        outer = A[:left] + A[right + 1:]
        inner.sort()
        outer.sort(reverse=True)
        for i in range(k):
            if i >= len(inner) or i >= len(outer):
                break
            if inner[i] < outer[i]:
                inner[i] = outer[i]
            else:
                break
        best = max(best, sum(inner))
print(best)
