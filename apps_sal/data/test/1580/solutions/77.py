def main():
    (n, m) = list(map(int, input().split()))
    cards = [-1 for i in range(n)]
    mg = {}
    for i in range(n):
        mg[i + 1] = []
    for i in range(m):
        (x, y, z) = list(map(int, input().split()))
        mg[x].append(y)
        mg[y].append(x)
    ans = 0
    for i in range(n):
        if cards[i] == -1:
            ans += 1
            cards[i] = 0
            que = [i]
            while len(que) > 0:
                s = que.pop(0)
                for v in mg[s + 1]:
                    if cards[v - 1] == 0:
                        continue
                    cards[v - 1] = 0
                    que.append(v - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
