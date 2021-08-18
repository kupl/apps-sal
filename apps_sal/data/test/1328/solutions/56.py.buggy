N, Ma, Mb = list(map(int, input().split()))
ABC = [tuple(map(int, input().split())) for _ in range(N)]
ABC.sort(key=lambda x: x[2])

dp = [[(0, 0, [-1])]]

for p in range(1, N * 100 + 1):
    tmp = []
    for i, (a, b, c) in enumerate(ABC):
        if p - c >= 0:
            for ta, tb, ti in dp[p - c]:
                if ti[-1] < i:
                    if (a + ta) * Mb == (b + tb) * Ma:
                        print(p)
                        return
                    tmp.append((a + ta, b + tb, ti + [i]))
    dp.append(tmp)

print("-1")
