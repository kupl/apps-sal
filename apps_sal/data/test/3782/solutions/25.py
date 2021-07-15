N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 10 ** 10

for a in A:
    candidates = []
    tmp = []
    for b in A:
        if a <= b:
            tmp.append(b)
        else:
            if K > 1:
                for i in sorted(tmp)[:-K+1]:
                    candidates.append(i)
            else:
                for i in sorted(tmp):
                    candidates.append(i)
            tmp = []
    if K > 1:
        for i in sorted(tmp)[:-K+1]:
            candidates.append(i)
    else:
        for i in sorted(tmp):
            candidates.append(i)
    candidates.sort()
    if len(candidates) >= Q:
        ans = min(ans, candidates[Q-1] - a)
print(ans)

