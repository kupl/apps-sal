N = int(input())
X = list(map(int, input().split()))
X.append(0)
load = 0
now = 0
for i in range(N + 1):
    load += abs(X[i] - now)
    now = X[i]
now = 0
for i in range(N):
    if now <= X[i] <= X[i + 1]:
        print(load)
    elif X[i + 1] <= X[i] <= now:
        print(load)
    else:
        ll = 2 * min(abs(X[i] - now), abs(X[i] - X[i + 1]))
        print(load - ll)
    now = X[i]
