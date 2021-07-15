q = int(input())
l = 0
r = 0
all_ = 0
arr = [0] * (1000000 * 2)
pos = [0] * 1000000
for i in range(q):
    s = input().split()
    id_ = int(s[1])
    op = s[0]
    if op == 'L':
        if all_ == 0:
            l = 1000001
            r = l + 1
        arr[l] = id_
        pos[id_] = l
        l -= 1
        all_ += 1
    if op == 'R':
        if all_ == 0:
            r = 1000001
            l = r - 1
        arr[r] = id_
        pos[id_] = r
        r += 1
        all_ += 1
    if op == '?':
        print(min(pos[id_] - l, r - pos[id_]) - 1)
