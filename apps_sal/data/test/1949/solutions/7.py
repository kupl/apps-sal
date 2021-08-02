def mi():
    return list(map(int, input().split()))


'''
3 5
1 2 3
'''
n, k = mi()
a = list(set(mi()))
n = len(a)
a.sort()
i = 0
res = 0
while k:
    k -= 1
    while i < n and a[i] <= 0:
        i += 1
    if i == n:
        print(0)
        continue
    a[i] -= res
    res += a[i]
    while i < n and a[i] <= 0:
        i += 1
    if i == n or a[i] <= 0:
        print(0)
        continue
    print(a[i])
    i += 1
'''
4 2
3 3 5 10
'''
