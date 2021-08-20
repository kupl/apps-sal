(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prefix = [0]
summ = 0
for i in range(n - 1):
    summ += a[i]
    prefix.append(summ)


def binsearch(x, a):
    left = 0
    right = len(prefix)
    while left != right - 1:
        mid = (left + right) // 2
        if x[mid] < a:
            left = mid
        else:
            right = mid
    return left


for i in range(m):
    q = binsearch(prefix, b[i])
    v = b[i] - prefix[q]
    print(q + 1, v)
