a = True
n, s = [int(x) for x in input().split()]
ph, pm = [int(x) for x in input().split()]

if ph*60 + pm >= s+1:
    print(0, 0)
    a = False
    return
for x in range(n - 1):
    h, m = [int(x) for x in input().split()]
    if h*60+m >= ph*60+pm + 2 + 2 * s:
        print((ph*60+pm+s+1) // 60, (ph*60+pm+s+1) % 60)
        a = False
        break
    else:
        ph = h
        pm = m
if a:
    print((ph*60+pm+s+1) // 60, (ph*60+pm+s+1) % 60)

