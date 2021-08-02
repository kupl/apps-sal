A, B = map(int, input().split())

for X in range(-100, 101):
    for Y in range(-100, 101):
        if X + Y == A and X - Y == B:
            print(X, Y)
