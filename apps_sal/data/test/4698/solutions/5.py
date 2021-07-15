N = int(input())
T = list(map(int,input().split()))
M = int(input())
for i in range(M):
    Pi,Xi=map(int,input().split())
    a = T[Pi-1]
    T[Pi-1] = Xi
    b = 0
    for j in range(N):
        b = b + T[j]
    print(b)
    T[Pi-1] = a
