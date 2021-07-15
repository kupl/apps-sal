n, k = [int(i) for i in input().split()]
a = input()
d = [[n + 1, 0] for i in range(26)]
for i in range(n):
    s = ord(a[i]) - ord('A')
    d[s][0] = min(d[s][0], i)
    d[s][1] = i
ev = []
for i in d:
    if i[0] != n + 1:
        ev.append([i[0], 0])
        ev.append([i[1], 1])
ev.sort()
b = 0
mb = 0
for i in range(len(ev)):
    if ev[i][1] == 1:
        b -= 1
    else:
        b += 1
    mb = max(mb, b)
print(['NO', 'YES'][int(mb > k)])

