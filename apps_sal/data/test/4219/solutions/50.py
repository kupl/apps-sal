def digitSum(n):
    s = str(bin(n))
    s = s[2:]
    array = list(map(int, s))
    return sum(array)
N = int(input())
A = []
X = []
Y = []
res = 0
for i in range(N):
    a = int(input())
    A.append(a)
    X_temp = []
    Y_temp = []
    for j in range(a):
        x,y = map(int,input().split())
        X_temp.append(x)
        Y_temp.append(y)
    X.append(X_temp)
    Y.append(Y_temp)
for i in range(1 << N):
    judge = True
    for j in range(N):
        if (i >> j) & 1:#もしAjが正直者だったら
            for k in range(A[j]):
                if (i >> X[j][k]-1) & 1 != Y[j][k]:
                    judge = False
        """else:#もしAjが不親切ものだったら。不親切者も正しいことをいうこともある。
            for k in range(A[j]):#
                if (i >> X[j][k]-1) & 1 == Y[j][k]:
                    judge = False"""
    if judge:
        res = max(res,digitSum(i))
print(res)
