l = []
for i in range(3):
    l += list(map(int, input().split()))
N = int(input())
b = set()
for i in range(N):
    c = int(input())
    if c in l:
        b.add(c)
for i in b:
    l[l.index(i)] = 0
if l[0] + l[1] + l[2] == 0 or l[3] + l[4] + l[5] == 0 or l[6] + l[7] + l[8] == 0:
    print('Yes')
    return
if l[0] + l[3] + l[6] == 0 or l[1] + l[4] + l[7] == 0 or l[2] + l[5] + l[8] == 0:
    print('Yes')
    return
if l[0] + l[4] + l[8] == 0 or l[2] + l[4] + l[6] == 0:
    print('Yes')
    return
print('No')
