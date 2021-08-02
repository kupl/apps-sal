q = int(input())
for i in range(q):
    w = int(input())
    if w < 3: print(4 - w)
    else:
        print(w % 2)
