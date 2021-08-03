from sys import stdin
input = stdin.readline

S, P = list(map(int, input().split()))
N = 1

can = 0
while(N * N <= P):
    if(P % N == 0):
        M = P // N

        if(M + N == S):
            can = 1
            break

    N += 1

print(("Yes" if can else "No"))
