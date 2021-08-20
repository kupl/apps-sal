(n, m, d) = map(int, input().split())
a = list(map(int, input().split()))
a = sorted([(a[i], i) for i in range(n)])
right = 0
left = 0
day = 0
ret = [0] * n
while right < n:
    if a[right][0] - a[left][0] <= d:
        day += 1
        ret[a[right][1]] = day
    else:
        ret[a[right][1]] = ret[a[left][1]]
        left += 1
    right += 1
print(day)
print(*ret)
