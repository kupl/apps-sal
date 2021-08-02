s = input()

w = 1

l = []

for c in s:
    if(len(l) == 0):
        l.append(c)
    elif(l[-1] == c):
        w = (w + 1) % 2
        l.pop()
    else:
        l.append(c)

if(w == 0):
    print("Yes")
else:
    print("No")
