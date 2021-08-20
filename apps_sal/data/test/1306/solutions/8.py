x = input().split()
n = int(x[0])
h = int(x[1])
x = input().split()
a = list((int(x[i]) for i in range(len(x))))
a.insert(0, h)
a.append(h)
sign = 0
way = 1
interval = []
start = []
end = {}
limit = 1000000007
for i in range(1, len(a)):
    if abs(a[i - 1] - a[i]) > 1 or a[i] > h:
        sign = 1
        break
    elif a[i] - a[i - 1] == -1:
        start.append(i)
    elif a[i] - a[i - 1] == 1:
        combination = len(start) - len(list(end.keys()))
        end[i - 1] = combination
    elif a[i] == a[i - 1] and a[i] < h:
        interval.append(i)
if sign == 1:
    print(0)
else:
    for i in range(len(interval)):
        way *= h - a[interval[i]] + 1
        if way > limit:
            way = way % limit
    for i in list(end.keys()):
        way *= end[i]
        if way > limit:
            way = way % limit
    print(way)
