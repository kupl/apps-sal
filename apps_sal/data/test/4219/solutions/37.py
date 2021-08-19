N = int(input())
A = []
xs = []
ys = []
X = []
Y = []
for i in range(N):
    a = int(input())
    A.append(a)
    for j in range(A[i]):
        (x, y) = map(int, input().split())
        xs.append(x)
        ys.append(y)
    X.append(xs)
    Y.append(ys)
    xs = []
    ys = []
B = []
ans = 0
count = 0
for i in range(2 ** N):
    B.append(format(i, 'b'))
for i in range(2 ** N):
    TF = ['0'] * N
    b = str(B[i])
    for j in range(len(b)):
        TF[-1 - j] = b[-1 - j]
    for j in range(N):
        if TF[j] == '1':
            for k in range(A[j]):
                if Y[j][k] == 1:
                    if TF[X[j][k] - 1] == '1':
                        continue
                    else:
                        count += 1
                if Y[j][k] == 0:
                    if TF[X[j][k] - 1] == '0':
                        continue
                    else:
                        count += 1
    if count <= 0:
        ans = max(ans, TF.count('1'))
    count = 0
print(ans)
