(l, r) = input().split()
l = int(l)
r = int(r)
cnt = 0
t = 1
while t <= r:
    t1 = t
    while t1 <= r:
        if t1 <= r and t1 >= l:
            cnt += 1
        t1 *= 3
    t *= 2
print(cnt)
