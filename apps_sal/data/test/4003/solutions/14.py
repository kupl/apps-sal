R = lambda: map(int, input().split())


def isL():
    k1 = 1
    while i + k1 <= j and a[i+k1]>a[i+k1-1]:
        k1 += 1
    k2 = 1
    while j - k2 >= i and a[j-k2]>a[j-k2+1]:
        k2 += 1
    return k1 >= k2


n, a = int(input()), list(R())
res = []
i, j = 0, n-1
v = 0
while i <= j:
    if a[i] <= v and a[j] <= v:
        break
    elif a[i] > v >= a[j]:
        res.append('L')
        v = a[i]
        i += 1
    elif a[j] > v >= a[i]:
        res.append('R')
        v = a[j]
        j -= 1
    elif a[i] < a[j]:
        res.append('L')
        v = a[i]
        i += 1
    elif a[j] < a[i]:
        res.append('R')
        v = a[j]
        j -= 1
    elif i == j:
        res.append('L')
        v = a[i]
        i += 1
    elif isL():
        res.append('L')
        v = a[i]
        i += 1
    else:
        res.append('R')
        v = a[j]
        j -= 1

res = ''.join(res)
print(len(res))
print(res)
