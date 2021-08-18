N = int(input())
S = [int(input()) for _ in range(N)]

S.sort()

s = sum(S)

if s % 10 == 0:
    for ss in S:
        if (s - ss) % 10 != 0:
            print(s - ss)
            return

    print(0)

else:
    print(s)
