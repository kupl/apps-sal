import sys


def main():
    input = sys.stdin.readline
    (n, c) = map(int, input().split())
    d = [0 for _ in range(c)]
    for i in range(c):
        d[i] = [int(x) for x in input().split()]
    grid = [0 for _ in range(n)]
    for i in range(n):
        grid[i] = [int(x) for x in input().split()]
    (k1, k2, k3) = ([0] * c, [0] * c, [0] * c)
    for i in range(n):
        for j in range(n):
            if (i + j) % 3 == 1:
                k1[grid[i][j] - 1] += 1
            elif (i + j) % 3 == 2:
                k2[grid[i][j] - 1] += 1
            else:
                k3[grid[i][j] - 1] += 1
    (key1, key2, key3) = ([], [], [])
    for i in range(c):
        (sub1, sub2, sub3) = (0, 0, 0)
        for j in range(c):
            if i == j:
                continue
            sub1 += k1[j] * d[j][i]
            sub2 += k2[j] * d[j][i]
            sub3 += k3[j] * d[j][i]
        key1.append([sub1, i])
        key2.append([sub2, i])
        key3.append([sub3, i])
    key1.sort()
    key2.sort()
    key3.sort()
    key1 = key1[:3]
    key2 = key2[:3]
    key3 = key3[:3]
    ans = pow(10, 9)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if key1[i][1] != key2[j][1] and key2[j][1] != key3[k][1] and (key1[i][1] != key3[k][1]):
                    if ans > key1[i][0] + key2[j][0] + key3[k][0]:
                        ans = key1[i][0] + key2[j][0] + key3[k][0]
    print(ans)


def __starting_point():
    main()


__starting_point()
