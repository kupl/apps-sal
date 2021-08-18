def main():
    import sys

    n, m = map(int, input().split())

    strs = [input() for _ in range(n)]
    scores = list(map(int, input().split()))

    ans = 0
    for i in range(m):
        cnt = [0] * 5
        for j in range(n):
            cnt[ord(strs[j][i]) - ord('A')] += 1
        ans += scores[i] * max(cnt)

    print(ans)

    return 0


main()
