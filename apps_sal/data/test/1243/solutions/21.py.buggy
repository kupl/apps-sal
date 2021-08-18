n = int(input())
lst = [*map(int, input().split())]
item = sum(lst) // n
if n == 1:
    print(0)
    return
less, more, leng1, leng2 = [], [], 0, 0
for i, x in enumerate(lst):
    if x < item:
        less.append(i)
        leng1 += 1
    if x > item:
        more.append(i)
        leng2 += 1
if leng1 == 0 and leng2 == 0:
    print(0)
    return
i, j = 0, 0
x, y = less[i], more[j]
res = 0
while i < leng1 and j < leng2:
    x, y = less[i], more[j]
    elem1 = lst[x]
    elem2 = lst[y]
    diff1 = item - elem1
    diff2 = elem2 - item
    if diff2 > diff1:
        res += (abs(x - y) * diff1)
        lst[y] -= diff1
        i += 1
    elif diff2 < diff1:
        res += (abs(x - y) * diff2)
        lst[x] += diff2
        j += 1
    else:
        res += (abs(x - y) * diff1)
        i, j = i + 1, j + 1
print(res)
