from collections import defaultdict


def main():
    (D, G) = map(int, input().split())
    problem = []
    for _ in range(D):
        (p, c) = map(int, input().split())
        problem.append([p, c])
    ans = float('inf')
    for i in range(2 ** D):
        all_solve = []
        others = []
        score = 0
        cnt = 0
        for j in range(D):
            if i >> j & 1:
                all_solve.append(j)
                cnt += problem[j][0]
                score += 100 * (j + 1) * problem[j][0] + problem[j][1]
            else:
                others.append(j)
        if score >= G:
            ans = min(cnt, ans)
            continue
        others.sort(reverse=True)
        for k in others:
            for m in range(problem[k][0]):
                score += 100 * (k + 1)
                cnt += 1
                if score >= G:
                    ans = min(ans, cnt)
                    break
            else:
                score += problem[k][1]
                if score >= G:
                    ans = min(ans, cnt)
            if score >= G:
                break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)


def __starting_point():
    main()


__starting_point()
