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
    (x, y, d) = input().split()
    (x, y) = (int(x), int(y))
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
if MR > max(MRp, MRm):
    t.append(MR - MRp)
elif MRm + MRp >= 2 * MR and MRm > MRp:
    t.append((MRm - MRp) / 2)
elif MRm > MRp:
    t.append(MRm - MR)
    t.append(MR - MRp)
if mR < min(mRp, mRm):
    t.append(mRm - mR)
elif mRm + mRp <= 2 * mR and mRm > mRp:
    t.append((mRm - mRp) / 2)
elif mRm > mRp:
    t.append(mRm - mR)
    t.append(mR - mRp)
if MU > max(MUp, MUm):
    t.append(MU - MUp)
elif MUm + MUp >= 2 * MU and MUm > MUp:
    t.append((MUm - MUp) / 2)
elif MUm > MUp:
    t.append(MUm - MU)
    t.append(MU - MUp)
if mU < min(mUp, mUm):
    t.append(mUm - mU)
elif mUm + mUp <= 2 * mU and mUm > mUp:
    t.append((mUm - mUp) / 2)
elif mUm > mUp:
    t.append(mUm - mU)
    t.append(mU - mUp)
ans = inf
for i in t:
    dx = max(MRp + i, MR, MRm - i) - min(mRp + i, mR, mRm - i)
    dy = max(MUp + i, MU, MUm - i) - min(mUp + i, mU, mUm - i)
    ans = min(ans, dx * dy)
print(ans)
