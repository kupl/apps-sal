N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

m1 = Y[N // 2 - 1]
m2 = Y[N // 2]

medians = [m2 if x < m2 else m1 for x in X]
print('\n'.join(map(str, medians)))
