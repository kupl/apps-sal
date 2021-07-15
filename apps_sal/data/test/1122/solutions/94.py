N, M = map(int, input().split())
if N%2:
    for i in range(M):
        print(i+1, N-i)
elif N%4:
    for i in range(M):
        if i < N//4:
            print(i+1, N-i-1)
        else:
            print(i+1, N-i-2)
else:
    for i in range(M):
        if i < N//4-1:
            print(i+1, N-i-1)
        else:
            print(i+1, N-i-2)
