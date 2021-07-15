S = [""] * 3
S[0] = input()
S[1] = input()
S[2] = input()
index = [0] * 3
turn = 0

while True:
    if index[turn] == len(S[turn]):
        print((chr(ord('A') + turn)))
        break
    else:
        nextTurn = ord(S[turn][index[turn]]) - ord('a')
        index[turn] += 1
        turn = nextTurn

