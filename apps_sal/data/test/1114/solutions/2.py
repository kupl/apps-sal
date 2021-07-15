import collections

n, m = map(int, input().split())
fs = list(map(int, input().split()))
bs = list(map(int, input().split()))

def solve(n, m, fs, bs):
    if not is_possible(n, m, fs, bs):
        print('Impossible')
        return
    ans = solve2(n, m, fs, bs)
    if not ans:
        print('Ambiguity')
    else:
        print('Possible')
        print(*ans)
        
def is_possible(n, m, fs, bs):
    setf = set(fs)
    setb = set(bs)
    return setb <= setf


def solve2(n, m, fs, bs):
    finv = collections.defaultdict(set)
    for i, f in enumerate(fs):
        finv[f].add(i)
    As = []
    for b in bs:
        fb = finv[b]
        if len(fb) > 1:
            return False
        for a in fb:
            As.append(a + 1)
    return As
    


solve(n, m, fs, bs)
