import math
s = input()
t = input()
lenS = len(s)
lenT = len(t)
yes = 0
no = 0


def change_register(l):
    if ord(l) > 96:
        return chr(ord(l) - 32)
    else:
        return chr(ord(l) + 32)


map1 = {}
for i in s:
    if map1.get(i, None) is None:
        map1[i] = 1
    else:
        map1[i] += 1
map2 = {}
for i in t:
    if map2.get(i, None) is None:
        map2[i] = 1
    else:
        map2[i] += 1
for i in map1:
    if map1.get(i, None) is None or map2.get(i, None) is None:
        continue
    diff = map1[i] - map2.get(i, 0)
    if diff > 0:
        yes += map1[i] - diff
        map2[i] -= map1[i] - diff
        map1[i] -= map1[i] - diff
    else:
        yes += map1[i]
        map2[i] -= map1[i]
        map1[i] = 0
for w in map1:
    i = change_register(w)
    if map1.get(w, None) is None or map2.get(i, None) is None:
        continue
    diff = map1[w] - map2.get(i, 0)
    if diff > 0:
        no += map1[w] - diff
        map2[i] = -(map1[w] - diff)
        map1[w] = -(map1[w] - diff)
    else:
        no += map1[w]
        map2[i] -= map1[w]
        map1[w] = 0
print(str(yes) + ' ' + str(no))
