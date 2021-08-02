__author__ = 'Krishna'

values = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0}
whiteStrength = 0
blackStrength = 0
for i in range(8):
    for piece in input():
        if ord('a') <= ord(piece) <= ord('z'):
            blackStrength += values.get(piece)
        elif ord('A') <= ord(piece) <= ord('Z'):
            whiteStrength += values.get(piece.lower())
if whiteStrength > blackStrength:
    print("White")
elif whiteStrength == blackStrength:
    print("Draw")
else:
    print("Black")
