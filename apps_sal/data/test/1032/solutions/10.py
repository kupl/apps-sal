n, p = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
a.sort()
result = []
_min = 0
for i in range(len(a) - 1, -1, -1):
    if _min <= a[i] - i:
        _min = a[i] - i

_max = a[-1]
for i in range(len(a) - 1, p-2, -1):
    if _max >= p - 2 - i + a[i]:
        _max = p - 2 - i + a[i]

result = max(_max - _min + 1, 0)
print(result)
if result > 0:
    for i in range(_min, _max + 1):
        print(i, end=' ')
""" print('max ', _max)
print('min ', _min) """

