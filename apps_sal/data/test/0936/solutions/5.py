n = int(input())
arr = [int(x) for x in input().split()]
m = -1
ans = -1
d = dict()
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    if m == -1 or d[i] > m:
        m = d[i]
        ans = i
print(ans)
