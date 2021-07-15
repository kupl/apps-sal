from collections import Counter

N = int(input())
A = list(map(int, input().split()))

L = [a+i for i, a in enumerate(A)]
R = [j-a for j, a in enumerate(A)]

L, R = Counter(L), Counter(R)

ans = 0

for k in L.keys():
    ans += L[k] * R[k]

print(ans)
