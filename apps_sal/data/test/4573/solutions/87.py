N = int(input())
X = list(map(int, input().split()))
a = sorted(X)[N // 2 - 1]
b = sorted(X)[N // 2]
if a == b:
    for _ in range(N):
        print(a)
else:
    for i in range(N):
        if X[i] <= a:
            print(b)
        else:
            print(a)
