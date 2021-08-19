(h, w) = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
c = [0] * (w * h)
k = 0
for (l, i) in enumerate(a):
    for j in range(i):
        c[k] = l + 1
        k += 1


def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]


ans = list(split_list(c, w))
for (i, j) in enumerate(ans):
    if i % 2 == 0:
        print(*j)
    else:
        print(*j[::-1])
