N, W = map(int, input().split())
Items = [tuple(map(int, input().split())) for _ in range(N)]
from collections import defaultdict as dd
Bag = dd(lambda:0)
Bag[0] = 0
for w,v in Items:
    temp = [(key+w,Bag[key]+v) for key in Bag if key + w <= W]
    for key,value in temp:
        Bag[key] = max(Bag[key],value)
ans = max(Bag.values())
print(ans)
