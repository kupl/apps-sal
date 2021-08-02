n = int(input())
l = list(map(int, input().strip().split()))
d = {}
arr = []
for i in l:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1
        arr.append(i)
arr.sort()
curr = arr[0] - 1
ans = 0
for j in arr:
    if curr < j:
        m = d[j]
        ans += (m * (m - 1)) // 2
        curr = j + m - 1
    else:
        m = d[j]
        pay = curr + 1 - j
        ans += pay * m + (m * (m - 1)) // 2
        curr = curr + m
print(ans)
