N = int(input())
X = list(map(int, input().split()))
X.sort()
if N % 2 != 0:
    print(X[N // 2])
else:
    left = sum([abs(x - X[N // 2 - 1]) for x in X])
    right = sum([abs(x - X[N // 2]) for x in X])
    if left <= right:
        print(X[N // 2 - 1])
    elif left > right:
        print(X[N // 2])

