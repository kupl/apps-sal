N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
d = []
for i in range(M - 1):
    d.append(X[i + 1] - X[i])
d.sort()
if M - N >= 0:
    print(sum(d[0:M - N]))
else:
    print(0)
