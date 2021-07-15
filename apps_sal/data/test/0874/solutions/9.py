n = int(input())
if n % 2 != 0:
    print(-1)
else:
    out = [0]*n
    t = True
    for i in range(n):
        if t:
            out[i+1] = i+1
            t = False
        else:
            out[i-1] = i+1
            t = True
    for i in range(n):
        print(out[i],end = " ")

