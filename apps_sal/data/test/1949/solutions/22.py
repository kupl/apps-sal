3
n, k = map(int, input().split())
values = sorted(set(map(int, input().split())))
prev = 0
distinct = min(len(values), k)
for i in range(distinct):
    print (values[i] - prev)
    prev = values[i]

for i in range(k - distinct):
    print (0)
