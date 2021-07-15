# mada dame datta.
def main():
    L = int(input())
    b = bin(L)[2:]
    bl = len(b)
    r = []
    for i in range(bl-1):
        r.append((i+1, i+2, 0))
        r.append((i+1, i+2, 2**i))
    if L == 2**(bl-1):
        pr(r)
        return
    end = bl
    for i in reversed(list(range(1, end))):
        if L - 2**(i-1) >= 2**(end-1):
            r.append((i, end, L-2**(i-1)))
            L -= 2**(i-1)
    pr(r)
def pr(r):
    m = 0
    for i in r:
        m = max(m, i[1])
    print((m, len(r)))
    for i in r:
        print((i[0], i[1], i[2]))
main()

