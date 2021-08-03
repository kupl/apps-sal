def fun(l, r, bound):
    nonlocal val
    ind = -1
    while(l <= r):
        mid = (l + r) // 2
        if (val[mid] >= bound):
            r = mid - 1
            ind = mid
        else:
            l = mid + 1
    return ind


n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    try:
        d[a[i]] += 1
    except:
        d[a[i]] = 1
val = list(d.values())
val.sort()
ans = 0
for i in range(1, 200100):
    temp = 0
    add = i
    ind = fun(0, len(val) - 1, add)
    while(ind != -1):
        temp += add
        add = add * 2
        ind = fun(ind + 1, len(val) - 1, add)
    ans = max(ans, temp)
print(ans)
