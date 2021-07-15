import sys
readline = sys.stdin.readline
N = int(readline())
if N == 1:
    print(0)
else:
    BN = 1
    while BN*2 <= N:
        BN*= 2
    Ans = []
    for i in range(BN.bit_length()):
        d = 1<<i
        for j in range(1, BN+1, 2*d):
            if j+d > BN:
                break
            for k in range(d):
                Ans.append((j+k, j+k+d))
    Ans = Ans + [(N+1-a, N+1-b) for a, b in Ans]
    print(len(Ans))
    print('\n'.join('{} {}'.format(*a) for a in Ans))
