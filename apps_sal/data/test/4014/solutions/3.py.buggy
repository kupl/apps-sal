n, m = list(map(int, input().split()))
prep = []

days = [-1] * n
release = []

for i in range(m):
    s_, d_, c_ = list(map(int, input().split()))
    release.append(s_)
    days[d_ - 1] = i
    prep.append(c_)

rel_on_day = {}
for i, r in enumerate(release):
    if r - 1 in rel_on_day:
        rel_on_day[r - 1].append(i)
    else:
        rel_on_day[r - 1] = [i]

ans = []

waiting = set()

exam_q = []
for d in days:
    if d != -1:
        exam_q.append(d)

# print(rel_on_day)

for i in range(n):
    if i in rel_on_day:
        waiting = waiting | set(rel_on_day[i])

 #   print(waiting)

    if days[i] != -1:  # exam
        if prep[days[i]] == 0:
            ans.append(m + 1)
            waiting.remove(days[i])
        else:
            print(-1)
            return
    else:  # choose closest unstudied exam
        chosen = None
        for ex in exam_q:
            if prep[ex] > 0 and ex in waiting:
                chosen = ex
                break
        if not chosen is None:
            prep[ex] -= 1
            ans.append(ex + 1)
        else:
            ans.append(0)

print(" ".join(list(map(str, ans))))
