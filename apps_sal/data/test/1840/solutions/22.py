from bisect import bisect_right


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i - 1
    return -1


s, b = list(map(int, input().split()))
v = []
a = list(map(int, input().split()))
for i in range(b):
    v.append(tuple(map(int, input().split())))
v.sort()
summa = 0
c = []
for i in v:
    summa += i[1]
    c.append(summa)

mas = [i[0] for i in v]

for i in a:
    ind = find_le(mas, i)
    if ind == -1:
        print(0)
    else:
        print(c[ind], end=' ')
