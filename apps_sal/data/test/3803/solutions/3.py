def R():
    return map(int, input().split())


(yH, yA, yD) = R()
(mH, mA, mD) = R()
(h, a, d) = R()
Q = 10 ** 20
for A in range(max(0, mD - yA + 1), max(0, mH + mD - yA) + 1):
    for D in range(max(0, mA - yD) + 1):
        H = yH - (mH + yA + A - mD - 1) // (yA + A - mD) * max(0, mA - yD - D)
        Q = min(A * a + D * d + max(0, h * (1 - H)), Q)
print(Q)
