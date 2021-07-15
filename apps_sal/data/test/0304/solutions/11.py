def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

fact = [1] * 1000
for i in range(2, 1000):
    fact[i] = fact[i - 1] * i

s = input()
cnt = {}
for d in '0123456789':
    cnt[int(d)] = s.count(d)
ans = 0

def getcnt(p):
    q = [pi for pi in p if pi != 0]
    num = fact[sum(q)]
    den = 1
    for qi in q:
        den *= fact[qi]
    gc = num // den
    if p[0]:
        q = [pi for pi in p if pi != 0]
        q[0] -= 1
        num = fact[sum(q)]
        den = 1
        for qi in q:
            den *= fact[qi]
        gc -= num // den
    #print(p, gc)
    return gc

def rec(d, p):
    nonlocal ans
    if d == 10:
        ans += getcnt(p)
        return
    if cnt[d] == 0:
        p[d] = 0
        rec(d + 1, p)
        return
    for c in range(1, cnt[d] + 1):
        p[d] = c
        rec(d + 1, p)

p = [0] * 10
rec(0, p)

print(ans)
