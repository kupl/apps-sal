n = int(input())
T = [0]
X = [0]
Y = [0]
judge = 'Yes'
for i in range(n):
    (t, x, y) = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
for i in range(1, n + 1):
    delt_t = T[i] - T[i - 1]
    t_parity = delt_t % 2
    d = abs(X[i] - X[i - 1]) + abs(Y[i] - Y[i - 1])
    d_parity = d % 2
    if delt_t >= d and t_parity == d_parity:
        continue
    else:
        judge = 'No'
        break
print(judge)
