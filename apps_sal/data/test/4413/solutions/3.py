Q = int(input())

for q in range(Q):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    y = 0
    for i in range(1, n):
        if L[i] - L[i - 1] == 1:
            y = 1
    if y == 1:
        print(2)
    else:
        print(1)
