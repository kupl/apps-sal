N = list(input())
N = [int(N[i]) for i in range(len(N))]
K = int(input())
if len(N) < K:
    for i in range(len(N)):
        if not N[i] == 1:
            print((N[i]))
            break
    else:
        print((1))
else:
    for i in range(K):
        if not N[i] == 1:
            print((N[i]))
            break
    else:
        print((1))
