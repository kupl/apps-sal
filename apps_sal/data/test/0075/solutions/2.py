def main():
    n, m = map(int, input().split())
    d = [[0] * m for i in range(n)]
    al = 0
    val_x = [0] * n
    val_y = [0] * m
    for i in range(n):
        s = input()
        cnt = 0
        for j in range(m):
            d[i][j] = s[j]
            cnt += (s[j] == '*')
            al += (s[j] == '*')
        val_x[i] = cnt
    for i in range(m):
        cnt = 0
        for j in range(n):
            cnt += (d[j][i] == '*')
        val_y[i] = cnt
    for i in range(n):
        for j in range(m):
            if val_x[i] + val_y[j] - (d[i][j] == '*') == al:
                print("YES")
                print(i + 1, j + 1)
                return
    print("NO")


main()
