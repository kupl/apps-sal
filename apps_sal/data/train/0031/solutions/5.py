t = int(input())
for tests in range(t):
    S = input().strip()
    ANS = 0
    Already = set()
    X = 0
    Y = 0
    for s in S:
        if s == 'N':
            if (X, Y, X, Y + 1) in Already:
                ANS += 1
            else:
                ANS += 5
            Already.add((X, Y, X, Y + 1))
            Already.add((X, Y + 1, X, Y))
            Y += 1
        elif s == 'S':
            if (X, Y, X, Y - 1) in Already:
                ANS += 1
            else:
                ANS += 5
            Already.add((X, Y, X, Y - 1))
            Already.add((X, Y - 1, X, Y))
            Y -= 1
        elif s == 'W':
            if (X, Y, X - 1, Y) in Already:
                ANS += 1
            else:
                ANS += 5
            Already.add((X, Y, X - 1, Y))
            Already.add((X - 1, Y, X, Y))
            X -= 1
        else:
            if (X, Y, X + 1, Y) in Already:
                ANS += 1
            else:
                ANS += 5
            Already.add((X, Y, X + 1, Y))
            Already.add((X + 1, Y, X, Y))
            X += 1
    print(ANS)
