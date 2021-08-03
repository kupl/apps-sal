from collections import Counter
import sys
read = sys.stdin.read


def main():
    def warshall_floyd(d):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d

    h, w = list(map(int, input().split()))
    n = 10
    d = []
    for _ in range(10):
        d.append(list(map(int, input().split())))
    d = warshall_floyd(d)
    a = []
    for _ in range(h):
        row = list(map(int, input().split()))
        row = [1 if i == -1 else i for i in row]
        a.extend(row)
    aa = Counter(a)
    ans = 0
    for i0 in range(10):
        ans += aa[i0] * d[i0][1]
    print(ans)


def __starting_point():
    main()


__starting_point()
