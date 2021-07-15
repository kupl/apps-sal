def count(a):
    res = 0
    delta = a[1] - a[0]

    for i in range(2, len(a)):
        e = a[i] - a[i - 1] - delta
        if abs(e) > 1:
            return -1

        if abs(e) == 1:
            a[i] -= e
            res += 1

    return res


n = int(input())
b = list(map(int, input().split()))
result = -1

if len(b) == 1:
    print(0)
    return

for i in range(-1, 2):
    for j in range(-1, 2):
        cb = b[:]
        cb[0] += i
        cb[1] += j

        cur = count(cb)

        if cur == -1:
            continue

        cur += abs(i) + abs(j)
        if result == -1 or (result != -1 and cur < result):
            result = cur

print(result)

