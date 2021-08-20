(n, k) = list(map(int, input().split()))
a = [(value, index) for (index, value) in enumerate(map(int, input().split()), 1)]
a.sort()
result = []
i = 0
while i < len(a) and k >= a[i][0]:
    result.append(a[i][1])
    k -= a[i][0]
    i += 1
print(len(result))
print(' '.join(map(str, result)))
