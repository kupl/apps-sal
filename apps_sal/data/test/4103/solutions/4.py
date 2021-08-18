N, B, A = list(map(int, input().split()))
maxA = A
S = [int(a) for a in input().split()]

for i in range(N):
    s = S[i]
    if A + B == 0:
        print(i)
        break
    else:
        if s > 0 and A < maxA and B > 0:
            B -= 1
            A += 1
        elif A > 0:
            A -= 1
        else:
            B -= 1
else:
    print(N)
