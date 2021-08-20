import heapq


def printn(x):
    return print(x, end='')


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


def inm():
    return map(int, input().split())


def ins():
    return input().strip()


DBG = True and False
BIG = 10 ** 18
R = 10 ** 9 + 7


def ddprint(x):
    if DBG:
        print(x)


(n, k, q) = inm()
a = inl()
mn = BIG
for i in range(n):
    lo = a[i]
    gr = []
    bg = -1
    for j in range(n):
        if lo <= a[j]:
            if bg < 0:
                bg = j
        elif bg >= 0:
            if j >= bg + k:
                gr.append((bg, j))
            bg = -1
    if bg >= 0 and n >= bg + k:
        gr.append((bg, n))
    ddprint(gr)
    h = []
    for (bg, ed) in gr:
        b = a[bg:ed]
        b.sort()
        for j in range(len(b) - k + 1):
            heapq.heappush(h, b[j])
    ddprint(h)
    if len(h) < q:
        continue
    mn0 = BIG
    mx = -1
    for j in range(q):
        v = heapq.heappop(h)
        mx = max(mx, v)
        mn0 = min(mn0, v)
    mn = min(mn, mx - mn0)
print(mn)
