from heapq import heappop, heappush
n = int(input())
c = 1
w = {}
wh = []
for i in input().split():
    i = int(i)
    w[i] = c
    c += 1
    heappush(wh, i)
o = ''
ss = []
for i in input():
    if i == '0':
        ss += [str(w[heappop(wh)])]
        o += ss[-1] + ' '
    else:
        o += ss[-1] + ' '
        ss.pop(-1)
print(o)
