from collections import defaultdict
from queue import *

n = int(input())
ratings = list(map(int, input().split(' ')))

value_ind_map = defaultdict(list)
# for i in range(len(ratings)):
#     value_ind_map[ratings[i]].put(i)
res = [-1]
txt = []
for rating in sorted(ratings):

    if res[0] >= rating:
        res[0] = res[0] + 1
        value_ind_map[rating].append(res[0])
    else:
        res[0] = rating
        value_ind_map[rating].append(res[0])
for rating in ratings:
    txt.append(str(value_ind_map[rating].pop()))

print(" ".join(txt))
