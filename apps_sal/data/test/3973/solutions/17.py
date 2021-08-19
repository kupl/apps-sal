from itertools import accumulate
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * (m + 2)
for (i, j) in zip(a, a[1:]):
    if j > i + 1:
        l[j + 1] -= 1
        l[i + 2] += 1
    elif i > j:
        if i <= m - 2:
            l[i + 2] += 1
            l[m + 1] -= 1
            l[1] += 1
            l[j + 1] -= 1
        else:
            l[i + 2 - m] += 1
            l[j + 1] -= 1
l = list(accumulate(l))
ans = 0
l1 = 0
for (i, j) in zip(a, a[1:]):
    if j > i:
        ans += j - i
        l[j + 1] -= j - i - 1
    else:
        l1 += m - i
        ans += m + j - i
        l[j + 1] -= m + j - i - 1
l[1] = l1
l = list(accumulate(l))
print(ans - max(l[1:m + 1]))
