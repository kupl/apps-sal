N = int(input())
A = list(map(int,input().split()))
A.sort()
mod = 10**9 + 7
if N%2 == 0:
    for i in range(N):
        if A[i] != 1+(i//2)*2:
            print(0)
            break
    else:
        print(pow(2,N//2,mod))
else:
    if A[0] == 0:
        for i in range(1,N):
            if A[i] != ((i+1)//2)*2:
                print(0)
                break
        else:
            print(pow(2,N//2,mod))
