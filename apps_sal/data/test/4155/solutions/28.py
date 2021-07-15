n = int(input())
h = list(map(int,input().split()))
w = 0
a = True

while a:
    mizu = False
    if sum(h) == 0:
        a = False
        break

    w += 1
    for i in range(n):
        if h[i] != 0:
            h[i] -= 1
            mizu = True
        else:
            if mizu:
                break 


print(w)
