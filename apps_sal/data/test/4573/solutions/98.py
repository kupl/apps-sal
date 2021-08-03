n = int(input())
X = list(map(int, input().split()))
x = sorted(X)
l = x[n // 2 - 1]
r = x[n // 2]
for i in range(n):
    if X[i] <= l:
        print(r)
    else:
        print(l)
