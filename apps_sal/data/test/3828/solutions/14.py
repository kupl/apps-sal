n = int(input())
L = input().split()
IDX = (n + 2) * [0]


def max(a, b):
    if a > b:
        return a
    return b


(mx, act, last) = (0, 0, 0)
for i in range(n):
    IDX[int(L[i])] = i + 1
for i in range(1, n + 1):
    if IDX[i] > last:
        last = IDX[i]
        act += 1
    else:
        last = IDX[i]
        act = 1
    mx = max(mx, act)
print(n - mx)
