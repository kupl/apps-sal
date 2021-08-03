s = input()
w = 1
l = []
for c in s:
    if(len(l) == 0):
        l.append(c)
    elif(l[-1] == c):
        l.pop()
        if(w == 1):
            w = 2
        else:
            w = 1

    else:
        l.append(c)
if(w == 1):
    print("No")
else:
    print("Yes")
