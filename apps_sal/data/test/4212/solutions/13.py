from itertools import combinations_with_replacement as combi

N, M, Q = map(int, input().split())

a = [0] * 55
b = [0] * 55
c = [0] * 55
d = [0] * 55

for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

candidate = combi(range(1, M+1), N)

ans = 0

for A in candidate:
    score = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            score += d[i]

    ans = max(ans, score)

print(ans)
