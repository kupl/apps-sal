def main():
    K, S = list(map(int, input().split()))
    ans = 0
    for Z in range(0, K+1):
        if 0 <= S - Z <= 2*K:
            ans += min(2*K - (S - Z) + 1, S-Z + 1)
    print(ans)

def __starting_point():
    main()

__starting_point()
