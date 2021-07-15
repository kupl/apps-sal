n, k = [int(i) for i in input().split()]

K = 1 << k
p = [0] * K

for i in range(n):
    pi = [int(j) for j in input().split()]
    pc = sum(pi[j] << j for j in range(k))
    p[pc] += 1

s = [0] * k

def go(i0, used):
    if i0 >= K: return False
    if p[i0]:
        s0 = s[:]
        ok = True
        used += 1
        for j in range(k):
            f = (i0 >> j) & 1
            assert f == 0 or f == 1
            s[j] += (i0 >> j) & 1
            if s[j] * 2 > used: ok = False
        if ok: return True
        if go(i0+1, used): return True
        s[:] = s0
        used -= 1
    return go(i0+1, used)

ans = "YES" if go(0, 0) else "NO"
print(ans)
