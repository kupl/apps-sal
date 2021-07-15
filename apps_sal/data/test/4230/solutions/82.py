x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

l = x
r = x
while True:
    if (l not in p) and (r not in p):
        print(l)
        return
    elif l not in p:
        print(l)
        return
    elif r not in p:
        print(r)
        return
    l -= 1
    r += 1

