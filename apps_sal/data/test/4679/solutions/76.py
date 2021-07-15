sa = list(input())
sb = list(input())
sc = list(input())
turn = "a"
for i in range(len(sa+sb+sc)):
    if turn == "a":
        if len(sa) == 0:
            print("A")
            break
        else:
            turn = sa[0]
            sa.remove(sa[0])
    elif turn == "b":
        if len(sb) == 0:
            print("B")
            break
        else:
            turn = sb[0]
            sb.remove(sb[0])
    else:
        if len(sc) == 0:
            print("C")
            break
        else:
            turn = sc[0]
            sc.remove(sc[0])
