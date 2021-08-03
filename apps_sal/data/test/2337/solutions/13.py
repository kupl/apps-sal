def R(): return list(map(int, input().split()))


n, m = R()
a = R()
b = R()
i = j = 0
while i < n and j < m:
    if b[j] >= a[i]:
        i += 1
    j += 1
print(n - i)
