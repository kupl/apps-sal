from sys import stdin
input = lambda : stdin.readline().strip()

def main():
    N, K = list(map(int, input().split()))
    N = 2 * (N - 1)
    K = abs(K)
    ans = sum((1 + min(i + K, N - i - K)) * (1 + min(i, N - i)) for i in range(N - K + 1))
    print(ans)

def __starting_point():
    main()

__starting_point()
