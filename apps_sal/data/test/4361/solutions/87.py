def main():
    N, K = list(map(int, input().split()))
    h = []
    for _ in range(N):
        h.append(int(input()))
    h.sort()
    ans = pow(10, 10)
    for k in range(N-K+1):
        ans = min(ans, abs(h[k]-h[K-1+k]))
    print(ans)

def __starting_point():
    main()

__starting_point()
