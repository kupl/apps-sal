def Numb(a, k):
    if a == 0:
        return 0
    m = len(bin(a)) - 3
    if m + 1 < k:
        return 0
    if k == 1:
        return m + 1
    if m + 1 == k:
        return Numb(a & (1 << m) - 1, k - 1)
    return C[m][k] + Numb(a & (1 << m) - 1, k - 1)


s = input()
nDec = int(s, 2)
n = len(s)
k = int(input())
C = [[1], [1, 1]]
for i in range(n):
    tmp = [1]
    for j in range(1, i + 2):
        tmp.append(C[-1][j - 1] + C[-1][j])
    tmp.append(1)
    C.append(tmp)
if k == 0:
    print(1)
else:
    NumOfOp = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        NumOfOp[i] = NumOfOp[bin(i).count('1')] + 1
    res = 0
    for i in range(1, n + 1):
        if NumOfOp[i] == k - 1:
            res += Numb(nDec, i)
    if k == 1:
        res -= 1
    print(res % (10 ** 9 + 7))
