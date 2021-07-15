w, h = map(int, input().split())
u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())

while h > 0:
    if h == d1:
        w = max(0, w + h - u1)
    elif h == d2:
        w = max(0, w + h - u2)
    else:
        w += h
    h -= 1
    
print(w)    
