def black(a):
    m = 0
    for i in a:
        i = list(i)
        for ii in i:
            if ii == "r":
                m += 5
            if ii == "q":
                m += 9
            if ii == "b":
                m += 3
            if ii == "n":
                m += 3
            if ii == "p":
                m += 1
            if ii == "k":
                m += 0
    return m
def white(a):
    m = 0
    for i in a:
        i = list(i)
        for ii in i:
            if ii == "R":
                m += 5
            if ii == "Q":
                m += 9
            if ii == "B":
                m += 3
            if ii == "N":
                m += 3
            if ii == "P":
                m += 1
            if ii == "K":
                m += 0
    return m

b = []
i = 0
while i<8:
    a = input()
    b.append(a)
    i+=1
if white(b)>black(b):
    print("White")
if black(b)>white(b):
    print("Black")
if black(b)==white(b):
    print("Draw")

