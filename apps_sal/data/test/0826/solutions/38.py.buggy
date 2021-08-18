n = int(input())
LOW = 0
HIGH = n
r = 0
now = (LOW + HIGH) // 2
if n < 3:
    print(1)
    return
while 1:
    now = (LOW + HIGH) // 2
    cur = (now * (now + 1)) // 2
    nex = ((now + 1) * (now + 2)) // 2
    if cur <= n + 1 and n + 1 < nex:
        r = now
        break
    elif cur < n + 1:
        LOW = now
    else:
        HIGH = now
print(n - r + 1)
