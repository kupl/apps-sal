from itertools import accumulate
(N, K) = list(map(int, input().split()))
S = input()
q = []
pre = S[0]
ans = cnt = 0
for s in S:
    if pre != s:
        q.append(cnt)
        cnt = 1
        pre = s
    else:
        cnt += 1
q.append(cnt)
J = 2 * K + 1
acc = list(accumulate(q))
acc += [acc[-1]]
if len(q) <= J:
    ans = acc[-1] - 1
else:
    ans = acc[J - 1] - 1 + acc[-1] - acc[J] - (len(q) - J)
    for (i, a) in enumerate(acc):
        if i + J < len(q):
            tot = acc[i + J] - acc[i] - 1
            tot += acc[i] + acc[-1] - acc[i + J + 1] - (len(q) - J)
            if tot > ans:
                ans = tot
print(ans)
