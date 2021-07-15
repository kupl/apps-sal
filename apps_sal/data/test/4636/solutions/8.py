T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]

    L = 0
    R = N-1
    turn = 0
    previous = 0
    alice = 0
    bob = 0
    moves = 0

    while L <= R:
        eaten = 0
        while eaten <= previous and L <= R:
            if turn == 0:
                eaten += A[L]
                alice += A[L]
                L += 1
            else:
                eaten += A[R]
                bob += A[R]
                R -= 1
        previous = eaten
        turn = 1 - turn
        moves += 1

    print(moves, alice, bob)

