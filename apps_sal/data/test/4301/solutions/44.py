N = int(input())
A = [int(input()) for _ in range(N)]
Asorted = sorted(A)
Amax1 = Asorted[-1]
Amax2 = Asorted[-2]
for a in A:
    if a != Amax1:
        print(Amax1)
    else:
        print(Amax2)
