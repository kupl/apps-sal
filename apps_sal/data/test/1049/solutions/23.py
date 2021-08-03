n, d = [int(x) for x in input().split()]

L = [0] * (d + 1)
for i in range(d):
    X = input()
    if '0' in X:
        L[i] = 1 + L[i - 1]
    else:
        L[i] = 0
print(max(L))
