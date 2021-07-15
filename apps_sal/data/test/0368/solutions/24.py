white = { 'Q' : 9, 'R' : 5, 'B' : 3, 'N' : 3, 'P' : 1 , 'K' : 0 }
black = { 'q' : 9, 'r' : 5, 'b' : 3, 'n' : 3, 'p' : 1 , 'k' : 0 }

import string

white_w = 0
black_w = 0

for i in range(8):
    line = input()
    for c in line:
        if c != '.':
            if c in string.ascii_uppercase:
                white_w += white[c]
            else:
                black_w += black[c]

if white_w > black_w:
    print("White",end="")
elif white_w < black_w:
    print("Black",end="")
else:
    print("Draw",end="")
    

