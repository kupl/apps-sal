3

N, M = (int(x) for x in input().split())

S = []
for i in range(M):
    items = [int(x) - 1 for x in input().split()]
    S.append(items[1:])

P = [int(x) for x in input().split()]

ret = 0
for bit in range(2**N):
    on = [i for i in range(N) if bit & (1 << i)]
    ok = True
    for i in range(M):
        s = S[i]
        p = P[i]
        if sum(1 for switch in s if switch in on) % 2 != p:
            ok = False
            break
    if ok:
        ret += 1
print(ret)
