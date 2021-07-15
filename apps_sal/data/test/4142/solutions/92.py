def __starting_point():

    S = list(input())
    
    chk = True
    for i in range(len(S)):
        if i % 2 == 1:
            if S[i] == "R":
                chk = False
                break
        else:
            if S[i] == "L":
                chk = False
                break
    if chk:
        print("Yes")
    else:
        print("No")

__starting_point()
