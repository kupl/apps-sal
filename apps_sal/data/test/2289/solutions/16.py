n, q = map(int, input().split())
a = list(map(int, input().split()))
k = list(map(int, input().split()))


def bins(arr, start, end, v):
    # find index of biggest value less than or equal to v
    s, e = start, end
    result = -1

    while s < e:
        m = (s + e) // 2

        if arr[m] >= v:
            e = m
        else:
            result = m
            s = m + 1

    return s if a[s] <= v else s - 1


for i in range(1, len(a)):
    a[i] += a[i - 1]

# arrow strength
s = 0
result = []

for ki in k:
    s += ki

    standing = n - bins(a, 0, len(a) - 1, s) - 1

    if standing > 0:
        result.append(standing)
    else:
        result.append(n)

    if s >= a[-1]:
        s = 0

print('\n'.join(map(str, result)))
