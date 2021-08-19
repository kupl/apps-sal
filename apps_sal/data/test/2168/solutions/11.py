n = int(input())
m = 0
max_ = float('-inf')
max_i = 0
r = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    tmp = tmp[1:]
    r.append(tmp)
    if max(tmp) > max_:
        max_ = max(tmp)
        max_i = i
for (i, val) in enumerate(r):
    if i != max_i:
        m = m + (max_ - max(val)) * len(val)
print(m)
