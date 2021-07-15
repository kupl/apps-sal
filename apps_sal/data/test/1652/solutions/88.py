S = input()
t = len(S)
L = [("dream", 5), ("dreamer", 7), ("erase", 5), ("eraser", 6)]
while t > 0:
    for w, l in L:
        if S.rfind(w, 0, t) == t - l:
            t -= l
            break
    else:
        print("NO")
        break
else:
    print("YES")

