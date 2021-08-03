for TT in range(1, int(input()) + 1):
    n = int(input())
    a = input()
    b = input()
    l = [[x, y] for x, y in zip(a, b) if x != y]
    res = len(l) == 0
    if len(l) == 2:
        res = l[0] == l[1]
    print("Yes" if res else "No")
