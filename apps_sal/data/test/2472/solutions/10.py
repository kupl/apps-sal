n = int(input())
s = []
for i in range(n):
    (a, b) = map(int, input().split())
    s.append([b, a])
s.sort()
t = 0
ts = 0
for i in s:
    ts = i[0]
    t += i[1]
    if t > ts:
        print('No')
        break
else:
    print('Yes')
