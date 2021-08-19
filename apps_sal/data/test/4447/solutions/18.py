(n, m) = map(int, input().split())
a = list(map(int, input().split()))
k = int(n / m)
lis = [[] for i in range(m + 1)]
free = list()
for i in range(n):
    ele = a[i] % m
    lis[ele].append(i)
ans = 0
for i in range(2 * m):
    cur = i % m
    while len(lis[cur]) > k:
        ele = lis[cur].pop()
        free.append([ele, i])
    while len(lis[cur]) < k and free != []:
        (ele, mm) = free.pop()
        lis[cur].append(ele)
        a[ele] += i - mm
        ans += i - mm
print(ans)
for item in a:
    print(item, end=' ')
