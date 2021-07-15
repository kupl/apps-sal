from sys import stdin as fin
# fin = open("cfr417b.in", "r")

def f(i, csum, csl=True):
    nonlocal num_f, l_a, r_a, minv
    l, r = l_a[i], r_a[i]
    if i == num_f:
        csum += r if csl else l
        minv = min(minv, csum)
    else:
        f(i + 1, csum + m + 2, not csl)
        f(i + 1, csum + (r if csl else l) * 2 + 1, csl)
        # print(num_f)

n, m = list(map(int, fin.readline().split()))
arr = [list(int(sym) for sym in fin.readline().strip()) for i in range(n)]
csl = True
cnt = 0
# print(arr)
border = 0
for i in range(n):
    if 1 in arr[i]:
        break
    else:
        border += 1
l_a, r_a = [], []
num_f = -1
minv = float('inf')
for i in range(n - 1, border - 1, -1):
    if 1 in arr[i]:
        l = arr[i].index(1)
        r = list(reversed(arr[i])).index(1)
        l = (m + 2 - l - 1)
        r = (m + 2 - r - 1)
    else:
        l = r = 0
    # print(l, r, m + 2 - l - 1, csl)
    l_a.append(l)
    r_a.append(r)
    num_f += 1
    continue
if num_f > -1:
    f(0, 0)
    print(minv)
else:
    print(0)

