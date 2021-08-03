def price(N, K):
    Kn = input().split()
    Flag = False

    for i in range(N, 10 * N, 1):
        value = str(i)
        for j in range(K):
            if(Kn[j] not in value):
                Flag = True
            elif(Kn[j] in value):
                Flag = False
                break

        if(Flag == True):
            print(i)
            break


N, K = (int(x) for x in input().split())
price(N, K)
