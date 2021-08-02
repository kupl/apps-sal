__author__ = 'User'


def p(x):
    l = 0
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m][0] <= x:
            l = m
        else:
            r = m
    return l


def p2(x):
    l = -1
    r = n - 1
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m][0] < x:
            l = m
        else:
            r = m
    return r


n, d = list(map(int, input().split()))
arr = [0] * n
summ = [0] * n
s = 0
for i in range(n):
    arr[i] = tuple(map(int, input().split()))
arr.sort()
for i in range(n):
    summ[i] = s + arr[i][1]
    s += arr[i][1]
summ.append(0)
mx = 0
# print(arr)
c = 0
for i in arr:
    r = p(i[0] + (d - 1))
    l = p2(i[0])
    #print(l, r)
    s = summ[r] - summ[l - 1]
    # print(s)
    mx = max(mx, s)
print(mx)
# print(summ)
# print(p(70))
