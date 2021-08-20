a = list(input())
b = list(input())
c = list(input())
tgt = a.pop(0)
while True:
    if tgt == 'a':
        if a:
            tgt = a.pop(0)
        else:
            ans = 'A'
            break
    elif tgt == 'b':
        if b:
            tgt = b.pop(0)
        else:
            ans = 'B'
            break
    elif c:
        tgt = c.pop(0)
    else:
        ans = 'C'
        break
print(ans)
