(n, r) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
idx = 0
cb = -100000
ptr = 0
count = 0
flag = True
while idx < n:
    ptr = max(0, idx - r + 1)
    while ptr < min(n, idx + r):
        if a[ptr] == 1:
            cb = ptr
        ptr += 1
    if abs(idx - cb) >= r:
        print(-1)
        flag = False
        break
    else:
        count += 1
        idx = cb + r
if flag:
    print(count)
