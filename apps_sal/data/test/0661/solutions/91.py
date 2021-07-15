import sys
input = sys.stdin.buffer.readline

def main():
    M,K = map(int,input().split())
    if M == 0:
        if K == 0:
            print(0,0)
        else:
            print(-1)
    elif M == 1:
        if K == 0:
            print(0,0,1,1)
        else:
            print(-1)
    else:
        if 2**M <= K:
            print(-1)
        else:
            use = [i for i in range(2**M)]
            use.pop(K)
            _use = list(reversed(use))
            ans = use+[K]+_use+[K]
            print(*ans)

def __starting_point():
    main()
__starting_point()
