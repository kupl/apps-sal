n = int(input())
d = dict()
for i in range(n):
    a = input()
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
m = 0
for elem in d:
    m = max(m, d[elem])
print(m)
