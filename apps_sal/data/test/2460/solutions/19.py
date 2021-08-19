# n=int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def next(k, a):
    i = k + 1
    while a[i] != 1:
        i += 1
    return i


ans = [0] * (m + 1)

k = -1
k = next(k, b)
ans[1] = k
for i in range(2, m + 1):
    kk = next(k, b)
    for j in range(k + 1, kk):
        if a[j] - a[k] <= a[kk] - a[j]:
            ans[i - 1] += 1
        else:
            ans[i] += 1
    k = kk


ans[m] += (n + m - 1 - k)

for i in range(1, m + 1):
    print(ans[i], end=' ')
