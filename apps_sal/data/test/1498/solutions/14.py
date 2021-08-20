from collections import defaultdict
(n, q) = list(map(int, input().split()))
S = [0] * (n + 1)
S[0] = 1
s = n
L = defaultdict(list)
pre = -1
for i in range(q):
    (t, k, d) = list(map(int, input().split()))
    for j in range(pre, t):
        for l1 in L[j]:
            for l2 in l1:
                S[l2] = 0
                s += 1
    if s >= k:
        tmp = []
        for j in range(1, n + 1):
            if S[j] == 0:
                S[j] = 1
                tmp.append(j)
                if len(tmp) == k:
                    break
        s -= k
        L[t + d - 1].append(tmp)
        print(sum(tmp))
        pre = t
    else:
        print(-1)
        pre = t
