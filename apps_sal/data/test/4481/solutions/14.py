from operator import itemgetter
N = int(input())
S = []
for i in range(N):
    S.append(input())
S_set = set(S)
S_sorted = sorted(S)
S_sorted.append("null0")

cntlist = [[S_sorted[0], 1]]
j = 0
for i in range(len(S) - 1):
    if cntlist[j][0] != S_sorted[i + 1]:
        cntlist.append([S_sorted[i + 1], 1])
        j = j + 1
    else:
        cntlist[j][1] += 1

maxnum = 0
for i in range(len(cntlist)):
    maxnum = max(cntlist[i][1], maxnum)
cntlist_new = []
for i in range(len(cntlist)):
    if cntlist[i][1] == maxnum:
        cntlist_new.append(cntlist[i])
new_cnt = sorted(cntlist_new, key=itemgetter(0), reverse=False)

# print(S)
# print(S_sorted)
# print(cntlist_new)
# print(new_cnt)

for i in range(len(new_cnt)):
    print(new_cnt[i][0])
