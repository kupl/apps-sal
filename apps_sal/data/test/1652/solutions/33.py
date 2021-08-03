S = input()
pnt = len(S)
while pnt:
    tmp = pnt
    if pnt >= 7:
        if S[pnt - 7:pnt] == "dreamer":
            pnt -= 7
    if pnt >= 6:
        if S[pnt - 6:pnt] == "eraser":
            pnt -= 6
    if pnt >= 5:
        if S[pnt - 5:pnt] == "dream" or S[pnt - 5:pnt] == "erase":
            pnt -= 5
    if tmp == pnt:
        break
if pnt:
    print("NO")
else:
    print("YES")
