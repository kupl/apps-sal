L, A, B, M = map(int, input().split())
C = (L - 1) * B + A
mod = M
X, s = 0, A
now = A
data = [0] * 19
ruiseki = [0] * 19
Ami = (A - 1) // B
Cmi = C // B
for i in range(19):
    now = 10**i - 1
    if now < A:
        ruiseki[i] = 0
    elif now >= C:
        ruiseki[i] = L
    else:
        ruiseki[i] = (now - A) // B + 1


def mul33(A, B):
    nonlocal mod
    res = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            res[i][j] = sum([A[i][k] * B[k][j] % mod for k in range(3)])
    return res


def ruijou(vec, Cd):
    rui = dict()
    if Cd == 0:
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    now = vec
    ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    Cds = bin(Cd)[2:][::-1]
    for i in range(len(Cds)):
        if Cds[i] == "1":
            ans = mul33(ans, now)
        now = mul33(now, now)
    return ans


def mul(X, s, Cd, d):
    nonlocal mod
    nonlocal B
    vec = [[pow(10, d, mod), 0, 0], [1, 1, 0], [0, B, 1]]
    vec = ruijou(vec, Cd)
    Xc = X
    sc = s
    X = (Xc * vec[0][0] + sc * vec[1][0] + vec[2][0]) % mod
    s = (Xc * vec[0][1] + sc * vec[1][1] + vec[2][1]) % mod
    return X, s


for d in range(1, 19):
    Cd = ruiseki[d] - ruiseki[d - 1]
    X, s = mul(X, s, Cd, d)
print(X)
