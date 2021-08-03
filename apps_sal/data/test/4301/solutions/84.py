N = int(input())
S = [int(input()) for _ in range(N)]
A = sorted(S)

for i in range(N):
    if S[i] == A[-1]:
        if len(A) > 1:
            print((A[-2]))
        else:
            print((A[-1]))
    else:
        print((A[-1]))
