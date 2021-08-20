import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        (N, X) = [int(x) for x in input().split()]
        A = [int(x) for x in input().split()]
        if sum(A) % X != 0:
            print(N)
            continue
        ans = float('inf')
        for i in range(N):
            if A[i] % X != 0:
                ans = i + 1
                break
        for i in range(N):
            if A[-i - 1] % X != 0:
                ans = min(ans, i + 1)
                break
        if ans == float('inf'):
            print(-1)
        else:
            print(N - ans)


def __starting_point():
    main()


__starting_point()
