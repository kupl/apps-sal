import heapq


def score(init, cand):
    score = [0] * (n + 1)
    score[0] = sum(init)
    hp = init
    heapq.heapify(hp)
    for (i, ai) in enumerate(cand):
        if hp[0] < ai:
            min_a = heapq.heappop(hp)
            score[i + 1] = score[i] + (ai - min_a)
            heapq.heappush(hp, ai)
        else:
            score[i + 1] = score[i]
    return score


n = int(input())
a = list(map(int, input().split()))
minus_a = [-x for x in a[::-1]]
former_score = score(a[:n], a[n:2 * n])
latter_score = score(minus_a[:n], minus_a[n:2 * n])[::-1]
ans = max((x + y for (x, y) in zip(former_score, latter_score)))
print(ans)
