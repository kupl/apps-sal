
t = int(input())

for loop in range(t):

    n = int(input())

    s = input()

    x = 0
    y = 0

    dic = {}
    dic[(0,0)] = -1

    ansl = float("-inf")
    ansr = float("inf")

    for i,S in enumerate(s):

        if S == "L":
            x -= 1
        elif S == "R":
            x += 1
        elif S == "U":
            y += 1
        elif S == "D":
            y -= 1

        if (x,y) in dic:
            nowl = dic[(x,y)]
            nowr = i

            if nowr - nowl < ansr - ansl:
                ansl = nowl
                ansr = nowr
            
        dic[(x,y)] = i

    if ansr == float("inf"):
        print(-1)
    else:
        print(ansl+2,ansr+1)
       

