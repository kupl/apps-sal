from collections import Counter


N, A = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = [x - A for x in X]
L = Counter()
L[0] = 1

for y in Y:
    for key, value in list(L.items()):
        L[key + y] += value

print((L[0] - 1))
