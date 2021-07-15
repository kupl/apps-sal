__author__ = 'Michael Ilyin'


def prepare(a):
    na = []
    last = 0
    for i in range(0, len(a)):
        if last != a[i]:
            na.append(a[i])
            last = a[i]
    return na


header = input()
films = int(header[:header.find(' ')])
genres = int(header[header.find(' '):])
numbers = [int(x) for x in input().split()]
res = [[genre, 0] for genre in range(1, genres + 1)]
numbers = prepare(numbers)
films = len(numbers)

for i, obj in enumerate(numbers):
    if i == 0:
        res[obj - 1][1] += 1
        continue
    if i == films - 1:
        res[obj - 1][1] += 1
        continue
    if numbers[i - 1] == numbers[i + 1]:
        res[obj - 1][1] += 2
    else:
        res[obj - 1][1] += 1
res = sorted(res, key=lambda x: x[0], reverse=False)
res = sorted(res, key=lambda x: x[1], reverse=True)
print(str(res[0][0]))
