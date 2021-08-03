def main():
    h, w, n = map(int, input().split())
    dic = {}
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(max(2, a - 1), min(h, a + 2)):
            for j in range(max(2, b - 1), min(w, b + 2)):
                if (i, j) in dic:
                    dic[(i, j)] += 1
                else:
                    dic[(i, j)] = 1
    ans = [0] * 10
    cnt = 0
    for v in dic.values():
        ans[v] += 1
        cnt += 1
    ans[0] = (h - 2) * (w - 2) - cnt
    for i in range(10):
        print(ans[i])


def __starting_point():
    main()


__starting_point()
