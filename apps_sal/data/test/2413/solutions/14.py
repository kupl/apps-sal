for i in range(int(input())):
    N = int(input())
    X = input()
    First, Last = 0, 0
    Rooms = 0
    if '1' in X:
        First, Last = X.index('1'), X[::-1].index('1')
        First = N - First
        Last = N - Last
        print(max(First, Last) * 2)
    else:
        print(N)
# Caption: Contest Time
