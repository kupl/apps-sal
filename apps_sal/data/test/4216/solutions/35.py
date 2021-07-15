N = int(input())
M = int(pow(N,1/2))

for i in range(M,0,-1):
    if N%i == 0:
        print((len(str(N//i))))
        return

