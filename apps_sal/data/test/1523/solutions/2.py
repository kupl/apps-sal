(n, k) = list(map(int, input().split()))
ideal = list(map(str, input().split()))
relocation = list(map(int, input().split()))
jobs = {}
uqjobs = {}
extra_jobs = []
for i in range(n):
    uqjobs[ideal[i]] = 1
    try:
        jobs[str(ideal[i])].append(relocation[i])
    except:
        jobs[str(ideal[i])] = [relocation[i]]
for i in jobs:
    if len(jobs[i]) > 1:
        jobs[i].sort()
        for j in range(len(jobs[i]) - 1):
            extra_jobs.append(jobs[i][j])
missing = 0
summ = 0
extra_jobs.sort()
for i in range(k - len(uqjobs)):
    summ += extra_jobs[i]
print(summ)
