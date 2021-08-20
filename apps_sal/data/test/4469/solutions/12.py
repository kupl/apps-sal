q = int(input())
lm = 0
rm = 0
idx = {}
ans = []
for i in range(q):
    (c, id) = [s for s in input().split()]
    if i == 0:
        idx[id] = 0
    elif c == 'L':
        lm -= 1
        idx[id] = lm
    elif c == 'R':
        rm += 1
        idx[id] = rm
    elif c == '?':
        ans.append(min(idx[id] - lm, rm - idx[id]))
print(*ans, sep='\n')
