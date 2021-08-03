# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
# k1, k2, k3 = next(reader)
# a = list(next(reader))
# b = list(next(reader))
# c = list(next(reader))

k1, k2, k3 = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


def ceil(a, L, R, pivot):
    while L + 1 < R:
        m = (L + R) // 2
        if (a[m] > pivot):
            R = m
        else:
            L = m
    return R


def LIS(a, n):

    tails = [0 for _ in range(n + 1)]
    empty = 0

    tails[0] = a[0]
    empty = 1
    for i in range(1, n):
        if (a[i] < tails[0]):
            tails[0] = a[i]
        elif (a[i] >= tails[empty - 1]):
            tails[empty] = a[i]
            empty += 1
        else:
            tails[ceil(tails, -1, empty - 1, a[i])] = a[i]

    return empty


n = k1 + k2 + k3
abc = [None] * n
for el in a:
    abc[el - 1] = 1
for el in b:
    abc[el - 1] = 2
for el in c:
    abc[el - 1] = 3
# print(abc)
print(n - LIS(abc, n))

# inf.close()
