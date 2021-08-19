(n, k) = map(int, input().split())
S = set()
D = dict()
for _ in range(n):
    (a, b) = map(int, input().split())
    if a in S:
        D[a] += b
    else:
        S.add(a)
        D[a] = b
L = sorted(S)
cnt = 0
for l in L:
    cnt += D[l]
    if cnt >= k:
        print(l)
        break
