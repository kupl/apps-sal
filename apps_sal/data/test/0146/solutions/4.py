n, k = list(map(int, input().split()))
arr = [int(x) for x in input().split()]


def calculate(a):
    nonlocal arr
    e, s = 0, 0
    for i in range(a, n, k):
        if arr[i] == -1:
            e += 1
        else:
            s += 1
    e -= arr.count(-1)
    s -= arr.count(1)
    return abs(e - s)


l = []
for i in range(k):
    l.append(calculate(i))
print(max(l))
