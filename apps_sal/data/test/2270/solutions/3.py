n = int(input())
a = list(map(int, input().split()))
q = int(input())
cnt8 = 0
cnt6 = 0
cnt4 = 0
cnt2 = 0
d = dict()
for i in a:
    d[i] = d.get(i, 0) + 1
for i in d.values():
    if i >= 8:
        cnt8 += 1
    if i >= 6:
        cnt6 += 1
    if i >= 4:
        cnt4 += 1
    if i >= 2:
        cnt2 += 1
for i in range(q):
    (t, val) = input().split()
    val = int(val)
    d[val] = d.get(val, 0)
    if d[val] >= 8:
        cnt8 -= 1
    if d[val] >= 6:
        cnt6 -= 1
    if d[val] >= 4:
        cnt4 -= 1
    if d[val] >= 2:
        cnt2 -= 1
    if t == '+':
        d[val] += 1
    else:
        d[val] -= 1
    if d[val] >= 8:
        cnt8 += 1
    if d[val] >= 6:
        cnt6 += 1
    if d[val] >= 4:
        cnt4 += 1
    if d[val] >= 2:
        cnt2 += 1
    if cnt8 >= 1:
        print('YES')
    elif cnt6 > 1 or (cnt6 == 1 and cnt2 >= 2):
        print('YES')
    elif cnt4 > 1 or (cnt4 == 1 and cnt2 >= 3):
        print('YES')
    else:
        print('NO')
