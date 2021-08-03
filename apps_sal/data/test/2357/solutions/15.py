def main():
    inf = 10**9
    T = int(input())
    Ans = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        L = [-inf] * (N + 1)
        ans = inf
        for i, a in enumerate(A):
            ans = min(ans, i - L[a])
            L[a] = i
        Ans.append(ans + 1 if ans < inf else -1)
    print("\n".join(map(str, Ans)))


main()
