A = input()
B = input()
C = input()

turn = 'a'
while True:
    num_card_A = len(A)
    num_card_B = len(B)
    num_card_C = len(C)
    if turn == 'a':
        if num_card_A == 0:
            winner = 'A'
            break
        turn = A[0]
        A = A[1:]
    elif turn == 'b':
        if num_card_B == 0:
            winner = 'B'
            break
        turn = B[0]
        B = B[1:]
    elif turn == 'c':
        if num_card_C == 0:
            winner = 'C'
            break
        turn = C[0]
        C = C[1:]

print(winner)
