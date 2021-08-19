(a, b) = list(map(int, input().split()))
if b % a == 0:
    c = b // a
    moves = 0
    while c % 2 == 0:
        c //= 2
        moves += 1
    while c % 3 == 0:
        c //= 3
        moves += 1
    if c == 1:
        print(moves)
    else:
        print(-1)
else:
    print(-1)
