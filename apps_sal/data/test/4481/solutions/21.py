n = int(input())
d = {}
max_value = 1
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
        max_value = max(max_value, d[s])
    else:
        d[s] = 1
l = []
for k in d:
    if d[k] == max_value:
        l.append(k)
for x in sorted(l):
    print(x)
