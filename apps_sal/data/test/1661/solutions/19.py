import bisect
(n, m) = input().strip().split(' ')
(n, m) = (int(n), int(m))
c = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))
i = 0
j = 0
cnt = 0
while i < n and j < m:
    if a[j] >= c[i]:
        cnt += 1
        i += 1
        j += 1
    else:
        i += 1
print(cnt)
