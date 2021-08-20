(numcand, numsub) = (int(i) for i in input().split())
subs = [[] for _ in range(numsub)]
for _ in range(numcand):
    (sub, prof) = (int(i) for i in input().split())
    subs[sub - 1].append(prof)
for sub in subs:
    sub.sort(reverse=True)
subs = [sub for sub in subs if sub and sub[0] > 0]
best = 0
while subs:
    best = max(best, sum((sub[0] for sub in subs)))
    for i in reversed(list(range(len(subs)))):
        if len(subs[i]) == 1 or subs[i][0] + subs[i][1] <= 0:
            subs.pop(i)
        else:
            subs[i][0:2] = [subs[i][0] + subs[i][1]]
print(best)
