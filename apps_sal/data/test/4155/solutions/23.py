n = int(input())
h = list(map(int,input().split()))

cnt = 0

def hana(h) :
    nonlocal cnt
    if len(h) == 0 :
        return
    if len(h) == 1 :
        cnt += h[0]
        return
    m = min(h)
    cnt += m
    h = [i - m for i in h ]
    while 0 in h :
        hana(h[:h.index(0)])
        h = h[h.index(0) + 1 :]
    hana(h)

hana(h)
print(cnt)

