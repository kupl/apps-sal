S = {}
S['a'] = input()
S['b'] = input()
S['c'] = input()
turn = 'a'
while True:
    hand = S[turn]
    if len(hand) == 0:
        break
    S[turn] = hand[1:]
    turn = hand[0]

print(turn.upper())
