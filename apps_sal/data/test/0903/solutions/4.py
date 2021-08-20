[n, k] = [int(w) for w in input().split()]
a = [int(w) for w in input().split()]
a.sort()
a.append(10 ** 57)
m = n // 2
for i in range(m, n):
    dk = (i - m + 1) * (a[i + 1] - a[i])
    if k < dk:
        break
    k -= dk
print(a[i] + k // (i - m + 1))
