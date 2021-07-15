from collections import defaultdict

n = int(input())
a = [int(i) for i in input().split()]

done = set()
d = defaultdict(int)

for i in a:
    d[i] += 1

c = len(list(d.keys()))
total = 0
for i in (a):
    d[i] -= 1
    if d[i] == 0:
        c -= 1

    if i not in done:
        total += c
        done.add(i)


print(total)



