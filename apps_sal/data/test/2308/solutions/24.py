t = int(input())
for _ in range(t) :
    x = input()
    y = input()
    ind = 0
    ind2 = 0
    for k in range(len(y)) :
        i = len(y)-1-k
        if y[i] == "1" :
            ind2 = k
            break
    for k in range(ind2, len(x)) :
        i = len(x)-1-k
        if x[i] == "1" :
            ind = k
            break
    print(max(0, ind-ind2))

