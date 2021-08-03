L = [0, 4, 1, 2, 3]
R = [0, 2, 3, 4, 1]
S = [0, 3, 4, 1, 2]

H = [0, 0, 0, 0, 0]
P = H[:]
for i in range(1, 5):
    l, s, r, p = list(map(int, input().split()))
    P[i] = p
    if 1 in [l, s, r]:
        H[i] = 1
    if l:
        H[L[i]] = 1
    if s:
        H[S[i]] = 1
    if r:
        H[R[i]] = 1
ans = "NO"
for i in range(1, 5):
    if P[i] and H[i]:
        ans = "YES"
print(ans)
