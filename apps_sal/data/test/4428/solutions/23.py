n = int(input())
a = list(map(int, input().split()))
(i, j, si, sj, r) = (-1, len(a), 0, 0, 0)
while i < j:
    if si == sj:
        r = si
    if si < sj:
        i += 1
        si += a[i]
    else:
        j -= 1
        sj += a[j]
print(r)
