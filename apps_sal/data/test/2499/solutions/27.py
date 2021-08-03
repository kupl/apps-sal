n = int(input())
l = list(map(int, input().split()))
e = []
sx = 0
for i in l:
    sx ^= i
for i in l:
    i &= (~sx)
    for j in e:
        i = min(i, i ^ j)
    if i:
        e.append(i)
t = 0
for i in e:
    t = max(t, t ^ i)
print((t ^ sx) + t)
