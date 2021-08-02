def main():
    read = lambda: list(map(int, input().split()))
    n = int(input())
    p = [tuple(read()) for i in range(n)]
    from collections import Counter
    cnt = Counter()
    for i in range(n):
        x, y = p[i][0], p[i][1]
        for j in range(i + 1, n):
            cnt[x + p[j][0], y + p[j][1]] += 1
    ans = sum(i * (i - 1) // 2 for i in list(cnt.values()))
    print(ans)


main()
