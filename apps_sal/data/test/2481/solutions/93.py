def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    h, w = map(int, input().split())
    c = [[int(i) for i in input().split()] for _ in range(10)]
    a = [[int(i) for i in input().split()] for _ in range(h)]

    # Warshall-Floyd
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if c[i][j] > c[i][k] + c[k][j]:
                    c[i][j] = c[i][k] + c[k][j]

    ans = 0
    for i in a:
        for j in i:
            if j == -1:
                continue
            else:
                ans += c[j][1]

    print(ans)

main()
