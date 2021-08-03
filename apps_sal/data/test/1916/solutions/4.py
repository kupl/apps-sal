n, m = list(map(int, input().split()))
ln = list(map(int, input().split()))
lm = list(map(int, input().split()))

for ans in range(512):
    poss = True
    for i in ln:
        curr = False
        for j in lm:
            if (i & j) | ans == ans:
                curr = True
        if curr == False:
            poss = False

    if poss == True:
        print(ans)
        break
