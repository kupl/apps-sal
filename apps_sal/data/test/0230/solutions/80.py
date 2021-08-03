N = int(input())
S = input()

MOD = 2 ** 61 - 1
root = 10000

rhs = [0]
for h in map(ord, S):
    rhs.append((root * rhs[-1] + h) % MOD)

pws = [1]
for i in range(N):
    pws.append(pws[-1] * root % MOD)

ok = 0
ng = N
while ng - ok > 1:
    mid = (ok + ng) // 2
    hashes = dict()
    flg = False
    for i in range(N - mid + 1):
        hashofsub = (rhs[i + mid] - rhs[i] * pws[mid]) % MOD
        if hashofsub in hashes:
            if i >= hashes[hashofsub] + mid:
                flg = True
                break
        else:
            hashes[hashofsub] = i

    if flg:
        ok = mid
    else:
        ng = mid

print(ok)
