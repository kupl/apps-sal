L = int(input())
str_A = (input())

#str_A  = str(A)

lens = len(str_A)

if lens % L == 0 and str_A != ("9"*lens):
    #print(1)
    build = -1
    for i in range(L,lens):
        if str_A[i] < str_A[i%L]:
            build =0
            break
        elif str_A[i] > str_A[i%L]:
            build = 1
            break
    if build in (1,-1):
        print(str(int(str_A[:L])+1)*(lens//L))
    if build == 0:
        print(str_A[:L] * (lens // L))

else:
    perf = ("1" + "0"*(L-1))*(lens// L +1)
    print(perf)
