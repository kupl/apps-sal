(n, k, m, t) = map(int, input().split())
pos = k
l = n
for tt in range(t):
    (ty, val) = map(int, input().split())
    if ty == 0:
        if val < pos:
            pos = pos - val
            l = l - val
        else:
            l = val
    else:
        l += 1
        if val <= pos:
            pos += 1
    print(l, pos)
