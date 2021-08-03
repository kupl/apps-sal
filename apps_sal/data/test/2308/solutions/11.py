import sys
input = sys.stdin.readline

T = int(input())
x = []
y = []
for i in range(2 * T):
    if i % 2 == 0:
        x.append(input())
    else:
        y.append(input())

for i in range(T):
    n = len(y[i])
    for j in range(n):
        if y[i][n - j - 1] == '1':
            break
    n = len(x[i])
    for k in range(j, n):
        if x[i][n - k - 1] == '1':
            break
    print(k - j)
