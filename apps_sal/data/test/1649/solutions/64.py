from itertools import permutations, combinations
import copy
a, b, c, d = map(int, input().split())

w = [a, b, c, d]

flag = False
for i in range(1, 4):
    for j in combinations(w, i):
        x = copy.copy(w)
        for k in j:
            x.pop(x.index(k))
        if sum(list(j)) == sum(x):
            print('Yes')
            flag = True
            break
    if flag:
        break
else:
    print('No')
