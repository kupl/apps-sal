S = input()
Q = int(input())
upside_down = False
front = ""

for i in range(Q):
    l = list(map(str, input().split()))

    if l[0] == "1":
        if upside_down == False:
            upside_down = True
        else:
            upside_down = False
    else:
        F, C = l[1], l[2]

        if upside_down:
            if F == "1":
                S = S + C
            else:
                front += C
        else:
            if F == "1":
                front += C
            else:
                S = S + C

front = front[::-1]
S = front + S

if upside_down:
    S = S[::-1]

print(S)
