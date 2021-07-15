def solve():
    on1 = 1
    on2 = 2
    off = 3
    for i in range(int(input())):
        win = int(input())
        if win == on1:
            on2, off = off, on2
        elif win == on2:
            on1, off = off, on1
        else:
            return 'NO'

    return 'YES'
print(solve())
