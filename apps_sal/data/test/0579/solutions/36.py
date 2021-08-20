from itertools import accumulate
(N, K) = list(map(int, input().split()))
P = list(map(int, input().split()))
C = list(map(int, input().split()))
P = [p - 1 for p in P]
check = [False] * N
ans = -float('inf')
for i in range(N):
    if not check[i]:
        score = []
        stop = i
        while 1:
            check[i] = True
            score.append(C[i])
            if P[i] == stop:
                break
            i = P[i]
        length = len(score)
        for j in range(length):
            if j != 0:
                score = score[1:] + [score[0]]
            ac = list(accumulate(score))
            if sum(score) <= 0:
                ans = max(ans, max(ac[:min(K, length)]))
            elif K % length == 0:
                ans = max(ans, ac[-1] * (K // length - 1) + max(ac))
            else:
                ans = max(ans, ac[-1] * (K // length) + max(ac[:K % length]))
print(ans)
