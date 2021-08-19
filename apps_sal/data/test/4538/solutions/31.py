import math
(N, D) = map(int, input().split())
X = [input() for i in range(N)]
count = 0
for i in range(N):
    X_list = list(map(int, X[i].split()))
    if D >= math.sqrt(X_list[0] ** 2 + X_list[1] ** 2):
        count += 1
print(count)
