(N, M) = map(int, input().split())
X = list(map(int, input().split()))
xs = sorted(X)
d = []
for i in range(M - 1):
    d.append(xs[i + 1] - xs[i])
ds = sorted(d)
if M > N:
    print(sum(ds[:M - N]))
else:
    print(0)
