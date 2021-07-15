def cumsum(itr):
    arr = []
    val = 0
    for x in itr:
        val += x
        arr.append(val)
    return arr


def main(N, scores):
    M = N - 1

    def max_score(d):
        steps = (scores[i] + scores[-i - 1] for i in range(0, M - d, d))
        cum_scores = cumsum(steps)

        if M % d > 0:
            return max(cum_scores)
        else:
            k = M // d + 1
            return max(cum_scores[: k // 2])

    corner_case = scores[0] + scores[M]
    otherwise = max(max_score(d) for d in range(1, M))
    return max(corner_case, otherwise)


N = int(input())
scores = [int(a) for a in input().split()]
result = main(N, scores)

print(result)
