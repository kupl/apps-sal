(a, k) = input().split()
k = int(k)
a = [i for i in a]
i = 0
while k > 0 and i < len(a):
    m = a[i:i + k + 1].index(max(a[i:i + k + 1]))
    if a[i + m] > a[i]:
        k -= m
        for j in range(i + m, i, -1):
            (a[j], a[j - 1]) = (a[j - 1], a[j])
    i += 1
print(''.join(a))
