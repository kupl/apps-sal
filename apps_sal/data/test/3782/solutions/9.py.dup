import sys
input = sys.stdin.readline


def main():
    n, k, q = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = [[v, i]for i, v in enumerate(a)]
    b.sort()
    index = [0] * n
    for i in range(n):
        index[i] = b[i][1]

    judge = [[] for i in range(n)]
    already = [-1, n]

    for i in range(n):

        for j in range(len(already) - 1):
            key = a[already[j] + 1:already[j + 1]]
            if len(key) >= k:
                judge[i].append(key)
        already.append(index[i])
        already.sort()

    ans = 1e9
    for i in range(n):
        if not judge[i]:
            break
        m = b[i][0]
        sub = []
        for values in judge[i]:
            values.sort()
            for j in range(len(values) - k + 1):
                sub.append(values[j])
        sub.sort()
        if len(sub) < q:
            break
        M = sub[q - 1]
        ans = min(ans, M - m)

    print(ans)


def __starting_point():
    main()


__starting_point()
