n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0
s = sum(d.values())
if s % 2 == 0:
    print(n - s)
else:
    print(n - s - 1)
