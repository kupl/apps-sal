def __starting_point():

    n = int(input())
    res = [n]*(2*n)

    if n % 2 == 0:
        for i in range(1,n+1,2):
            index = i//2
            res[index] = i
            res[n-1-index] = i

        for i in range(2,n+1,2):
            index = i//2-1
            res[n+index] = i
            res[2*n-2-index] = i

    else:
        m = n//2*2
        for i in range(2,n+1,2):
            index = i//2-1
            res[index] = i
            res[m-1-index] = i
        #print(" ".join(map(str,res)))

        for i in range(1,n+1,2):
            index = i//2
            res[m+index] = i
            res[2*n-2-index] = i
        #print(" ".join(map(str,res)))

    print(" ".join(map(str,res)))

__starting_point()
