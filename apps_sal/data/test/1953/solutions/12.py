def f(l, key):
    l = l - 1
    r = len(arr)
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(*arr)
s = 0
c = 0
i = 0
while i < n:
    if arr[i] >= s:
        s += arr[i]
        i += 1
        c += 1
    else:
        i = f(i, s)
print(c)
