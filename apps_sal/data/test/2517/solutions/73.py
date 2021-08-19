def main():
    from sys import stdin
    input = stdin.readline
    (n, m, r) = list(map(int, input().split()))
    l = [int(i) - 1 for i in input().split()]
    d = [[10 ** 8] * n for _ in range(n)]
    for _ in range(m):
        (i, j, k) = list(map(int, input().split()))
        d[i - 1][j - 1] = k
        d[j - 1][i - 1] = k
    for k in range(n):
        for i in range(n - 1):
            for j in range(i + 1, n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    d[j][i] = d[i][j]
    from itertools import permutations
    answer = float('inf')
    for i in permutations(l):
        ans = 0
        for j in range(r - 1):
            ans += d[i[j]][i[j + 1]]
        if ans < answer:
            answer = ans
    print(answer)


main()
