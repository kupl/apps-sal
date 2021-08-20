w = input()
w_set = set(w)
d = {}
for i in w_set:
    d[i] = 0
for i in w:
    d[i] += 1
for i in d.values():
    if i % 2 != 0:
        print('No')
        break
else:
    print('Yes')
