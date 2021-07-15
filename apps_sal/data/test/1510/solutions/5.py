n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort(); b.sort()
i = j = 0
s = t = sum(b)
while True:
    if i == n or (j < m and a[i] > b[j]): 
        if j == m: break
        x = b[j]
        j += 1
    else:
        x = a[i]
        i += 1
    t -= x
    s = min(t - x * (m - j - i), s)
print(s)
