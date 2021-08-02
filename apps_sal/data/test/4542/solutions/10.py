S = input()
# 0回判定
x = len(S)
if S.count("B") == x or S.count("W") == x:
    print(0)
    return


cntw = 0
for s in S.split("W"):
    if s:
        cntw += 1
cntb = 0
for s in S.split("B"):
    if s:
        cntb += 1
print(abs(cntb - cntw) + min(cntb, cntw) * 2 - 1)
