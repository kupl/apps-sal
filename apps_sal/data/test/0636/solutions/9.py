(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sorted(a)
result = []
days_used = 0
for i in range(n):
    if days_used + b[i] <= k:
        days_used += b[i]
        result.append(a.index(b[i]) + 1)
        a[a.index(b[i])] = 0
    else:
        break
print(len(result))
print(' '.join((str(i) for i in result)))
