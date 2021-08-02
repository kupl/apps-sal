from collections import defaultdict
import heapq
N, K = map(int, input().split())

hq = []
tset_all = set()
for i in range(N):
    t, d = map(int, input().split())
    heapq.heappush(hq, (-d, t))
    tset_all.add(t)
# print(heapq)

hq_K = []
dsum = 0
tdic = defaultdict(int)
for i in range(K):
    md, t = heapq.heappop(hq)
    heapq.heappush(hq_K, ((-md, t)))
    dsum -= md
    tdic[t] += 1

t0 = len(tdic)
max_answer = dsum + (t0**2)
# print(t0,max_answer)

for i in range(t0 + 1, min(K, len(tset_all)) + 1):
    loop_flg = True
    while(loop_flg):
        d, t = heapq.heappop(hq_K)
        if tdic[t] > 1:
            tdic[t] -= 1
            dsum -= d

            while(True):
                md2, t2 = heapq.heappop(hq)
                if tdic[t2] == 0:
                    tdic[t2] = 1
                    dsum -= md2
                    loop_flg = False
                    break

    answer_i = dsum + (i**2)
    # print(i,answer_i)
    max_answer = max(max_answer, answer_i)

print(max_answer)
