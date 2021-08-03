from collections import Counter

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

accA = [0] * (N + 1)
for i, a in enumerate(A, start=1):
    accA[i] = (accA[i - 1] + a) % M

cntS = Counter()
ans = 0
for s in accA:
    ans += cntS[s]
    cntS[s] += 1

print(ans)
