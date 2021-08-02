def r(): return list(map(int, input().split()))


n, d = r()
a = sorted(tuple(r()) for i in range(n))

i = 0
Min = a[i][0]
Max = cur = 0

for m, s in a:
    cur += s
    if m - Min >= d:
        while m - a[i][0] >= d:
            cur -= a[i][1]
            i += 1
        Min = a[i][0]
    Max = max(Max, cur)

print(Max)
