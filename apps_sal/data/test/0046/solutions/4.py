

n, m = list(map(int, input().split()))

nMod = [n // 5] * 5
mMod = [m // 5] * 5

for loop in range(1, n % 5 + 1):
    nMod[loop] += 1

for loop in range(1, m % 5 + 1):
    mMod[loop] += 1

print(nMod[0] * mMod[0] + nMod[1] * mMod[4] + nMod[4] * mMod[1] + nMod[2] * mMod[3] + nMod[3] * mMod[2])
