import copy
S = input()
ListS = list(S)
revListS = copy.deepcopy(ListS)
norm = 0
rev = 0
N = len(ListS)
for i in range(1, N):
    if ListS[i] == ListS[i - 1]:
        ListS[i] = str(abs(int(ListS[i]) - 1))
        norm += 1
    if revListS[N - i - 1] == revListS[N - i]:
        revListS[N - i - 1] = str(abs(int(revListS[N - i - 1]) - 1))
        rev += 1
res = min(norm, rev)
print(res)
