q = int(input())
for i in range(q):
    lrd = input().split()
    for j in range(3):
        lrd[j] = int(lrd[j])
    l = lrd[0]
    r = lrd[1]
    d = lrd[2]
    if d < l:
        print(d)
    else:
        print(d * (r // d + 1))
