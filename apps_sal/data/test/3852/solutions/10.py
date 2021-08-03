n = int(input())
a = list(map(int, input().split()))

maxi = max(list(range(n)), key=lambda x: a[x])
maxa = a[maxi]
mini = min(list(range(n)), key=lambda x: a[x])
mina = a[mini]
out = []
if maxa > -mina:
    for i in range(1, n):
        while a[i] < a[i - 1]:
            out.append((maxi + 1, i + 1))
            a[i] = a[i] + maxa
        if a[i] > maxa:
            maxa = a[i]
            maxi = i
else:
    for i in range(n - 2, -1, -1):
        while a[i + 1] < a[i]:
            out.append((mini + 1, i + 1))
            a[i] = a[i] + mina
        if a[i] < mina:
            mina = a[i]
            mini = i

print((len(out)))
for o in out:
    print((o[0], o[1]))
