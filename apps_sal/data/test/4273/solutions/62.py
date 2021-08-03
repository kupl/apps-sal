import itertools
n = int(input())
march = dict()

a = "MARCH"
for i in range(5):
    march[a[i]] = 0

for i in range(n):
    s = input()
    if s[0] in march:
        march[s[0]] += 1

res = 0
for i in itertools.combinations("MARCH", 3):
    tmp = 1
    for j in i:
        tmp *= march[j]
    res += tmp

print(res)
