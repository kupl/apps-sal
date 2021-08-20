from collections import defaultdict
d = defaultdict(int)
N = int(input())
N_List = list(map(int, input().split()))
for i in range(N):
    CN = N_List[i]
    for k in range(-1, 2, 1):
        d[CN + k] += 1
print(max(d.values()))
