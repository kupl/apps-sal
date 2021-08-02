
def main():
    n, m = map(int, input().split(" "))
    ls = [{} for _ in range(n)]
    h = list(map(int, input().split(" ")))
    for i in range(n):
        ls[i] = [h[i]]
    ab = []
    for i in range(m):
        ab.append(list(map(lambda i: int(i) - 1, input().split(" "))))
    for i in range(m):
        if ls[ab[i][0]][0] >= ls[ab[i][1]][0]:
            ls[ab[i][1]].append(ls[ab[i][0]][0] + 1)
        if ls[ab[i][1]][0] >= ls[ab[i][0]][0]:
            ls[ab[i][0]].append(ls[ab[i][1]][0] + 1)
    cnt = 0
    for i in range(n):
        if ls[i][0] == max(ls[i]):
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
