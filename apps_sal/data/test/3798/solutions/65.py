import math

N = int(input())
S = int(input())
L = N-S

def search(b, n=N):
    ans = 0
    while n >= b:
        ans += n%b
        n //= b
    ans += n
    return ans


def main():

    if L < 0:
        print(-1)
    elif L == 0:
        print(N+1)
    else:
        P = []
        for l in range(1, int(math.sqrt(L))+2):
            if L%l == 0:
                P.append(l+1)
                P.append(L//l+1)
        P.sort()

        ans = -1
        for p in P:
            if p == 1: continue
            S0 = search(p)
            if S == S0:
                ans = p
                break

        print(ans)

def __starting_point():
    main()
__starting_point()
