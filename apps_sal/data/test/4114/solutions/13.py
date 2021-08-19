n = int(input())
hs = [list(map(int, input().split())) for _ in range(n)]
hs.sort(key=lambda x: x[2], reverse=True)


def main():
    for x in range(101):
        for y in range(101):
            height = hs[0][2] + abs(x - hs[0][0]) + abs(y - hs[0][1])
            for i in range(1, n):
                if max(height - (abs(x - hs[i][0]) + abs(y - hs[i][1])), 0) == hs[i][2]:
                    pass
                else:
                    break
                if i == n - 1:
                    print(x, y, height)
                    return (x, y, height)


main()
