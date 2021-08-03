n = int(input())
C = [int(s) for s in input().split(" ")]
A = [int(s) - 1 for s in input().split(" ")]
al = [False for i in range(0, n)]
ans = 0
for v in range(0, n):
    if al[v]:
        continue
    sequence = []
    while not al[v]:
        sequence.append(v)
        al[v] = True
        v = A[v]
    if v in sequence:
        tek = C[v]
        for j in sequence[sequence.index(v) + 1:]:
            tek = min(C[j], tek)
        ans += tek
print(ans)
