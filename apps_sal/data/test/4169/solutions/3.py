n, m = list(map(int, input().split()))

C = {}
S1 = []
for i in range(n):
    a, b = list(map(int, input().split()))
    S1.append(a)
    if a in C:
        C[a] += b
    else:
        C[a] = b
S = list(set(S1))
S.sort()

ans = 0
for s in S:
    if m < C[s]:
        ans += m * s
        break
    else:
        ans += C[s] * s
        m -= C[s]

print(ans)
