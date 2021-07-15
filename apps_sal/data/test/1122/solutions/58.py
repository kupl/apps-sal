def resolve():
    N,M = map(int,input().split())
    if N % 2 == 1:
        for i in range(M):
            print(str(i+1) + " " + str(N-i))
    else:
        for i in range((M-1) // 2 + 1):
            print(str(i+1) + " " + str(N-i))
        for i in range((M-1) // 2 + 1 , M):
            print(str(i+1) + " " + str(N-i-1))
resolve()
