N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()

x = sum(S)
if x % 10 != 0:
    print(x)
else:
    for i in range(N):
        if(x - S[i]) % 10 != 0:
            print((x - S[i]))
            break
    else:
        print((0))
