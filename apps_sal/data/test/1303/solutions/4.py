def inter(A, B, t):
    for i in B:
        if i + t in A:
            return True
    return False


(p, q, r, l) = list(map(int, input().split()))
X = set()
Z = set()
for i in range(p):
    (b, e) = list(map(int, input().split()))
    for i in range(b, e + 1):
        Z.add(i)
for i in range(q):
    (b, e) = list(map(int, input().split()))
    for i in range(b, e + 1):
        X.add(i)
cnt = 0
for i in range(r, l + 1):
    if inter(Z, X, i):
        cnt += 1
print(cnt)
