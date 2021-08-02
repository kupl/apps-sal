n = int(input())
l = []
while n:
    m = [int(i) for i in input().split(" ")]
    l.append((m[0], m[1]))
    n -= 1
d = {}
for i in l:
    d[i] = 0
for i in l:
    d[i] += 1
print(max(d.values()))
