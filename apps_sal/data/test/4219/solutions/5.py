n = int(input())
a = []
x = []
y = []
for i in range(n):
    ai = int(input())
    a.append(ai)
    xi = []
    yi = []
    for j in range(ai):
        (xij, yij) = list(map(int, input().split(' ')))
        xi.append(xij)
        yi.append(yij)
    x.append(xi)
    y.append(yi)
ans = 0
for case in range(2 ** n):
    truth_t = 0
    truth = 0
    for i in range(n):
        if case >> i & 1:
            truth_t += 1
            proof = 0
            for j in range(a[i]):
                if case >> x[i][j] - 1 & 1 == y[i][j]:
                    proof += 1
            if proof == a[i]:
                truth += 1
    if truth == truth_t:
        if ans < truth:
            ans = truth
print(ans)
