import copy

N = int(input())
X = list(map(int, input().split()))

x = copy.deepcopy(X)
x.sort()

x1 = x[N // 2 - 1]
x2 = x[N // 2]

for xx in X:
    if xx <= x1:
        print(x2)
    else:
        print(x1)
