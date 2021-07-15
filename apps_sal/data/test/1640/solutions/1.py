summ = 0
glob = 0
N = int(input())
a = {}
cnt = 0
huh = list(map(int, input().split()))
for i in huh:
    if i - 1 not in a:
        a[i - 1] = 0
    if i + 1 not in a:
        a[i + 1] = 0
    if i not in a:
        a[i] = 0
    glob += (cnt - a[i - 1] - a[i + 1]) * i - (summ - a[i - 1] * (i - 1) - a[i + 1] * (i + 1))
    a[i] += 1
    summ += i
    cnt += 1
print(glob)
