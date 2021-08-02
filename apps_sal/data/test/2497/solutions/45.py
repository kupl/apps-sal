inf = float('inf')
N = int(input())
MRp = -inf
MR = -inf
MRm = -inf
mRp = inf
mR = inf
mRm = inf
MUp = -inf
MU = -inf
MUm = -inf
mUp = inf
mU = inf
mUm = inf

for i in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    if d == 'R':
        MRp = max(MRp, x)
        mRp = min(mRp, x)
        MU = max(MU, y)
        mU = min(mU, y)
    elif d == 'L':
        MRm = max(MRm, x)
        mRm = min(mRm, x)
        MU = max(MU, y)
        mU = min(mU, y)
    elif d == 'U':
        MUp = max(MUp, y)
        mUp = min(mUp, y)
        MR = max(MR, x)
        mR = min(mR, x)
    else:
        MUm = max(MUm, y)
        mUm = min(mUm, y)
        MR = max(MR, x)
        mR = min(mR, x)

t = [0]
if MR > MRp:
    t.append(MR - MRp)
if MRm > MRp:
    t.append((MRm - MRp) / 2)
if MRm > MR:
    t.append(MRm - MR)
if mRm > mR:
    t.append(mRm - mR)
if mRm > mRp:
    t.append((mRm - mRp) / 2)
if mR > mRp:
    t.append(mR - mRp)
if MU > MUp:
    t.append(MU - MUp)
if MUm > MUp:
    t.append((MUm - MUp) / 2)
if MUm > MU:
    t.append(MUm - MU)
if mUm > mU:
    t.append(mUm - mU)
if mUm > mUp:
    t.append((mUm - mUp) / 2)
if mU > mUp:
    t.append(mU - mUp)

ans = inf
for i in t:
    dx = max(MRp + i, MR, MRm - i) - min(mRp + i, mR, mRm - i)
    dy = max(MUp + i, MU, MUm - i) - min(mUp + i, mU, mUm - i)
    ans = min(ans, dx * dy)
print(ans)
