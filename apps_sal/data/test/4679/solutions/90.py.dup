SA = input()
SB = input()
SC = input()

indexA = 0
indexB = 0
indexC = 0
turn = 'A'
winner = ''
while 1:
    if turn == 'A':
        if indexA == len(SA):
            winner = 'A'
            break
        if SA[indexA] == 'a':
            turn = 'A'
        elif SA[indexA] == 'b':
            turn = 'B'
        elif SA[indexA] == 'c':
            turn = 'C'
        indexA += 1
    elif turn == 'B':
        if indexB == len(SB):
            winner = 'B'
            break
        if SB[indexB] == 'a':
            turn = 'A'
        elif SB[indexB] == 'b':
            turn = 'B'
        elif SB[indexB] == 'c':
            turn = 'C'
        indexB += 1
    elif turn == 'C':
        if indexC == len(SC):
            winner = 'C'
            break
        if SC[indexC] == 'a':
            turn = 'A'
        elif SC[indexC] == 'b':
            turn = 'B'
        elif SC[indexC] == 'c':
            turn = 'C'
        indexC += 1
print(winner)
