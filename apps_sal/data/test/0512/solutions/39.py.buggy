#from collections import deque,defaultdict
def printn(x): return print(x, end='')
def inn(): return int(input())
def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353


def ddprint(x):
    if DBG:
        print(x)


def leaf(x, y):
    nonlocal hl
    if (x, y) in hl:
        return hl[(x, y)]
    m = (y - x) // 2
    for aa, bb in pairs:
        if aa < x < bb or aa < y < bb or (x <= aa < bb <= y and bb - aa != m):
            hl[(x, y)] = False
            return False
    for i in range(m):
        if bl[x + i] or al[x + m + i]:
            hl[(x, y)] = False
            return False
    hl[(x, y)] = True
    return True


def dfs(x, y):
    nonlocal hd
    if leaf(x, y):
        return True
    if y - x == 2:
        return False
    if (x, y) in hd:
        return hd[(x, y)]
    for aa, bb in pairs:
        if aa < x < bb or aa < y < bb:
            hd[(x, y)] = False
            ddprint(f"dfs {x=} {y=} F")
            return False
    for i in range(x + 2, y, 2):
        if dfs(x, i) and dfs(i, y):
            hd[(x, y)] = True
            ddprint(f"dfs {x=} {y=} T")
            return True
    hd[(x, y)] = False
    ddprint(f"dfs {x=} {y=} F2")
    return False


n = inn()
al = [False] * (2 * n)
bl = [False] * (2 * n)
aonly = []
bonly = []
pairs = []
for i in range(n):
    a, b = inm()
    a -= 1
    b -= 1
    if a >= 0 and (al[a] or bl[a]) or b >= 0 and (al[b] or bl[b]):
        print('No')
        return
    if a >= 0:
        al[a] = True
        if b < 0:
            aonly.append(a)
    if b >= 0:
        bl[b] = True
        if a < 0:
            bonly.append(b)
    if a >= 0 and b >= 0:
        if a >= b:
            print('No')
            return
        pairs.append((a, b))

ddprint(al)
ddprint(bl)
ddprint(pairs)

chged = True
while chged:
    ddprint("chg loop")
    chged = False
    for aa in aonly:
        ddprint(f"{aa=}")
        dela = False
        for i in range(len(pairs)):
            ap, bp = pairs[i]
            ddprint(f"{i=} {ap=} {bp=}")
            if ap < aa < bp:
                bb = aa + bp - ap
                if bb >= 2 * n or al[bb] or bl[bb]:
                    ddprint(f"{bb=}")
                    print('No')
                    return
                pairs.append((aa, bb))
                bl[bb] = True
                chged = True
                dela = True
                break
        if dela:
            aonly.remove(aa)
            break

    for bb in bonly:
        delb = False
        for i in range(len(pairs)):
            ap, bp = pairs[i]
            if ap < bb < bp:
                aa = bb - (bp - ap)
                if aa < 0 or al[aa] or bl[aa]:
                    print('No')
                    return
                al[aa] = True
                pairs.append((aa, bb))
                delb = True
                chged = True
                break
        if delb:
            bonly.remove(bb)
            break

hd = {}
hl = {}
print('Yes' if dfs(0, 2 * n) else 'No')
