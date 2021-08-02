from collections import Counter

N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))
V.sort(reverse=True)

S = sum(V[:A])
cnt = A
mx = S / cnt
L = [cnt]

for v in V[A:]:
    if cnt == B:
        break
    cnt += 1
    S += v
    if mx < S / cnt:
        mx = S / cnt
        L = []
    if mx == S / cnt:
        L.append(cnt)


def ncr(n, r):
    ret = 1
    for i in range(r):
        ret *= (n - i)
    for i in range(1, r + 1):
        ret //= i
    return ret


print(mx)
ans = 0
cntV = Counter(V)
for c in L:
    cnt = Counter(V[:c])
    prd = 1
    for x, c in list(cnt.items()):
        prd *= ncr(cntV[x], c)
    ans += prd
print(ans)
