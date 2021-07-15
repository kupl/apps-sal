n = int(input())
for i in range(n):
    q = int(input())
    qq = str(q)
    L = len(qq)
    w = (L-1)*9
    for i in range(1, 10):
        if q>=int(str(i)*L):
            w+=1
        else:
            break
    print(w)

