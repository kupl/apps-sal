D = {4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
N = int(input())
A = [D[int(a)] for a in input().split()]
X = [0] * 6
for a in A:
    if a == 0:
        X[a] += 1
    else:
        if X[a - 1]:
            X[a - 1] -= 1
            X[a] += 1
print(N - X[5] * 6)
