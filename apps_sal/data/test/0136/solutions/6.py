def preprocess(g):
    g = input()
    g = list(g)
    r = len(g)-1
    for i in range(0,len(g)):
        if g[i] > '0':
            r = i
            break
    g = g[r:]
    return "".join(g)
[g,h] = [1,1]
g = preprocess(g)
h = preprocess(h)
if len(g) < len(h):
    print("<")
elif len(g) > len(h):
    print(">")
else:
    if g < h:
        print("<")
    elif g > h:
        print(">")
    else:
        print("=")

