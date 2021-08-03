from statistics import median

X = []
X1 = []
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    X.append(a)
    X1.append(b)

m1 = median(X)
m2 = median(X1)
if len(X) % 2:
    print(int((m2 - m1) + 1))
else:
    print(int(2 * (m2 - m1) + 1))
