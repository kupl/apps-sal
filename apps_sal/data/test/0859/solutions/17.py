s1 = input()
s2 = input()
P = s1.count("+") - s1.count("-")
C = s2.count("+") - s2.count("-")
Goal = abs(P - C)
Cnt = s2.count("?")
K = [[0] * 21 for i in range(11)]
K[0][10] = 1.0
for i in range(1, Cnt + 1):
    for j in range(0, 21, 1):
        if j - 1 >= 0:
            K[i][j] += K[i - 1][j - 1] * 0.5
        if j + 1 <= 20:
            K[i][j] += K[i - 1][j + 1] * 0.5
if Goal + 10 <= 20: print(K[Cnt][Goal + 10])
else: print(0.0)
