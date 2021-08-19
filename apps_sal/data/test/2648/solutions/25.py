from collections import Counter
N = int(input())
A = list(sorted(map(int, input().split()), reverse=True))
cnt_a = Counter(A)
X = [0] * 3
for (k, v) in list(cnt_a.items()):
    while v >= 3:
        v = v // 3 + v % 3
    X[v] += 1
if X[2] % 2 == 0:
    print(X[1] + X[2])
else:
    print(X[1] - 1 + X[2])
