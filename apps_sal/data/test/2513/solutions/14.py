N = int(input())
s = list(str(input()))

x = [0]*N
v = ["S","W"]

for x[0],x[1] in [["S","S"],["S","W"],["W","S"],["W","W"]]:
    for i in range(2,N):
        if (x[i-1] =="S" and s[i-1] == "o") or (x[i-1] =="W" and s[i-1] == "x"):
            x[i] = x[i-2]
        else:
            if x[i-2] == "S":
                x[i] = "W"
            else:
                x[i] = "S"
    #print(x)
    det = 0
    if (x[N-1] == "S" and s[N-1] == "o" and x[N-2] != x[0]):
        det = -1
    elif (x[N-1] == "S" and s[N-1] == "x" and x[N-2] == x[0]):
        det = -1
    elif (x[N-1] == "W" and s[N-1] == "o" and x[N-2] == x[0]):
        det = -1
    elif (x[N-1] == "W" and s[N-1] == "x" and x[N-2] != x[0]):
        det = -1
    elif (x[0] == "S" and s[0] == "o" and x[N-1] != x[1]):
        det = -1
    elif (x[0] == "S" and s[0] == "x" and x[N-1] == x[1]):
        det = -1
    elif (x[0] == "W" and s[0] == "o" and x[N-1] == x[1]):
        det = -1
    elif (x[0] == "W" and s[0] == "x" and x[N-1] != x[1]):
        det = -1
    
    if det == 0:
        print(("".join(x)))
        break

if det == -1:
    print((-1))

