from collections import defaultdict
(N, K) = map(int, input().split())
alist = list(map(int, input().split()))
slist = [0]
for i in range(N):
    slist.append(slist[-1] + alist[i])
sslist = []
for i in range(N + 1):
    sslist.append((slist[i] - i) % K)
answer = 0
si_dic = defaultdict(int)
for i in range(N + 1):
    if i - K >= 0:
        si_dic[sslist[i - K]] -= 1
    answer += si_dic[sslist[i]]
    si_dic[sslist[i]] += 1
print(answer)
