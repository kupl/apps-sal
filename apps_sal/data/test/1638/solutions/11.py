from sys import stdin, stdout
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
dict = []
val = -1
i = 0
while i < n:
    v = a[i]
    j = i - 1
    arr = []
    pmin = v
    while j >= 0:
        v += min(a[j], pmin)
        arr.append(min(a[j], pmin))
        pmin = min(pmin, min(a[j], pmin))
        j -= 1

    arr = arr[::-1]
    arr.append(a[i])
    j = i + 1
    pmin = v
    while j < n:
        v += min(a[j], pmin)
        arr.append(min(a[j], pmin))
        pmin = min(pmin, min(a[j], pmin))
        j += 1
    if v > val:

        val = max(val, v)
        dict = arr
    i += 1
print(*dict)
# print(dict.values())
