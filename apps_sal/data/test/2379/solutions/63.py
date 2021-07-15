N, K, C = list(map(int, input().split()))
S = input()

work_day_min = []
work_day_max = []

for i in range(N):
    if S[i] == 'o':
        if i > 0 and len(work_day_min) > 0:
            if i - work_day_min[-1] <= C:
                continue
        work_day_min.append(i)
    if len(work_day_min) == K:
        break

for i in range(N):
    if S[N - i - 1] == 'o':
        if i > 0 and len(work_day_max) > 0:
            if work_day_max[-1] - (N - i - 1) <= C:
                continue
        work_day_max.append(N - i - 1)
    if len(work_day_max) == K:
        break

for i in range(K):
    if work_day_min[i] == work_day_max[K-i-1]:
        print(work_day_min[i]+1)
