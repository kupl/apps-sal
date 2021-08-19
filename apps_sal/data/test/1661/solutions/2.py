def mi():
    return map(int, input().split())


(n1, n2) = mi()
c = list(mi())
a = list(mi())
i = 0
j = 0
cnt = 0
while i < n1 and j < n2:
    cur = c[i]
    if cur <= a[j]:
        j += 1
        cnt += 1
    i += 1
print(cnt)
