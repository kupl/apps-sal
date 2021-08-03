sa = input()
sb = input()
sc = input()

turn = sa[0]
sa = sa[1:]
while True:
    if turn == "a":
        if sa == "":
            print("A")
            break
        else:
            turn = sa[0]
            sa = sa[1:]
    elif turn == "b":
        if sb == "":
            print("B")
            break
        else:
            turn = sb[0]
            sb = sb[1:]
    elif turn == "c":
        if sc == "":
            print("C")
            break
        else:
            turn = sc[0]
            sc = sc[1:]
