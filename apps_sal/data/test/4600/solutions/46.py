from collections import defaultdict as dc
n, m = [int(i) for i in input().split()]
cq_dic = {}
wa_dic = dc(int)
for _ in range(m):
    p, w = input().split()
    if w == 'AC':
        cq_dic[p] = 1
    elif (not p in cq_dic) and w == 'WA':
        wa_dic[p] += 1
ans = sum([wa_dic[k] for k in cq_dic])
print(len(cq_dic), ans)
