n, k = list(map(int, input().split()))
d = list(map(int, input().split()))

v = n
while True:
    f = True
    for t in list(str(v)):
        if int(t) in d:
            f = False
            continue
    if f:
        print(v)
        return
    v+=1

