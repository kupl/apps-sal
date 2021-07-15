import sys
input = sys.stdin.readline

def solve():
    H, W = map(int, input().split())
    G = [[ord(s) - 46 for s in input().strip()] for _ in range(H)]
    Gy = list(map(list, zip(*G)))
    k = 0
    St = [None]*77
    for h, G1 in enumerate(G, 1):
        k = max(k, max(G1))
        for w, g in enumerate(G1, 1):
            if not g:
                continue
            if St[g] is None:
                St[g] = (h, w)
            elif type(St[g]) == tuple:
                h1, w1 = St[g]
                if h == h1:
                    St[g] = h
                elif w == w1:
                    St[g] = -w
                else:
                    return False
            else:
                if St[g] == h or St[g] == -w:
                    continue
                return False
    if k == 0:
        return []
    A = []
    for j in range(k, 50, -1):
        if St[j] is None:
            A.append(A[-1])
            continue
        if type(St[j]) == tuple:
            A.append(St[j]*2)
            continue
        x = St[j]
        if x > 0:
            Gh = G[x-1]
            p = None
            e = None
            for ig, g in enumerate(Gh):
                if g == j:
                    p = ig
                    break
            for ig, g in enumerate(Gh[::-1]):
                ig = W - 1 - ig
                if g == j:
                    e = ig
                    break
            for ig in range(p, e + 1):
                if Gh[ig] < j:
                    return False
            A.append((x, p+1, x, e+1))
        else:
            Gw = Gy[-x-1]
            p = None
            e = None
            for ig, g in enumerate(Gw):
                if g == j:
                    p = ig
                    break
            for ig, g in enumerate(Gw[::-1]):
                ig = H - 1 - ig
                if g == j:
                    e = ig
                    break
            for ig in range(p, e + 1):
                if Gw[ig] < j:
                    return False
            A.append((p+1, -x, e+1, -x))
    
    return A[::-1]
    
def __starting_point():
    T = int(input())
    for _ in range(T):
        ans = solve()
        if ans is False:
            print('NO')
            continue
        print('YES')
        print(len(ans))
        for a in ans:
            print(*a)
__starting_point()
