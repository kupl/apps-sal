n, m = map(int, input().split())
minv = n
ming = m
maxv = 0
maxg = 0
i = 0
while (i < n):
    str = input()
    j = 0
    while (j < m):
        if (str[j] == '*'):
            if (minv > i):
                minv = i
            if (maxv < i):
                maxv = i
            if (ming > j):
                ming = j
            if (maxg < j):
                maxg = j
        j += 1
    i += 1
if ((maxv - minv) > (maxg - ming)):
    n = maxv - minv + 1
    print(n)
else:
    m = maxg - ming + 1
    print(m)
