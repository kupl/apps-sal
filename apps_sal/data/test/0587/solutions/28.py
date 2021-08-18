from collections import defaultdict
N, K = map(int, input().split())

dtlist = []
tset_all = set()
for i in range(N):
    t, d = map(int, input().split())
    dtlist.append((d, t))
    tset_all.add(t)
dtlist.sort()

dtlist_Krev = []
dsum = 0
tdic = defaultdict(int)
for i in range(K):
    d, t = dtlist.pop()
    dtlist_Krev.append((d, t))
    dsum += d
    tdic[t] += 1
dtlist_Krev.sort(reverse=True)

t0 = len(tdic)
max_answer = dsum + (t0**2)

for i in range(t0 + 1, min(K, len(tset_all)) + 1):
    loop_flg = True
    while(loop_flg):
        d, t = dtlist_Krev.pop()
        if tdic[t] > 1:
            tdic[t] -= 1
            dsum -= d

            while(True):
                d2, t2 = dtlist.pop()
                if tdic[t2] == 0:
                    tdic[t2] = 1
                    dsum += d2
                    loop_flg = False
                    break

    answer_i = dsum + (i**2)
    max_answer = max(max_answer, answer_i)

print(max_answer)
