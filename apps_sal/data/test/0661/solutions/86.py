def main():
    (M, K) = map(int, input().split())
    if K == 0:
        ans = []
        for i in range(2 ** M):
            ans.extend([i, i])
        print(*ans)
        return 0
    if 2 ** M <= K:
        print(-1)
        return 0
    if M == 1:
        if K == 1:
            print(-1)
            return 0
    ans = [str(x) for x in range(2 ** M) if x != K]
    ans_b = [str(x) for x in range(2 ** M - 1, -1, -1) if x != K]
    print(str(K) + ' ' + ' '.join(ans) + ' ' + str(K) + ' ' + ' '.join(ans_b))


main()
