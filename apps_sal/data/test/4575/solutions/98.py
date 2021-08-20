N = int(input())
(D, X) = map(int, input().split())
A = []
day = 1
for i in range(N):
    a = int(input())
    X += 1
    while True:
        day += a
        if day > D:
            break
        else:
            X += 1
    day = 1
print(X)
