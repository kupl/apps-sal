A,B,C = [input() for i in range(3)]
turn="a"

while True:
    if turn == "a":
        if A == "":
            print("A")
            break
        turn = A[0]
        A = A[1:]
    elif turn == "b":
        if B == "":
            print("B")
            break
        turn = B[0]
        B = B[1:]
    else:
        if C == "":
            print("C")
            break
        turn = C[0]
        C = C[1:] 
