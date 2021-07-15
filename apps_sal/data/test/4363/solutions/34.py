def main():
    K, S = list(map(int,input().split()))
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            if i+j <= S and S - (i+j) <= K:
                ans += 1
    print(ans)
def __starting_point():
    main()

__starting_point()
