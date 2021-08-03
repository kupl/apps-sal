from collections import deque

n = int(input())
l = [[int(i) - 1 for i in input().split()] for i in range(n)]
# 選手の番号をindexと一致させる

q = deque(list(range(n)))
days = [0 for i in range(n)]
pairs = [-1 for i in range(n)]
while q:
    a = q.popleft()  # qの左端の選手のindexをpopleft
    if len(l[a]) == 0:  # a番の選手のリクエストがない
        continue  # skip
    b = l[a].pop(0)
    # l[a]:a番の選手のリクエストリスト
    # l[a]の最初のリクエストをpop

    # a:ある選手のindex
    # b:a番の選手が最初にリクエストした選手のindex
    if pairs[b] == a:  # bのリクエストがaなら
        days[a] = days[b] = max(days[a], days[b]) + 1
        q.append(a)
        q.append(b)
    else:
        pairs[a] = b
print((max(days) if not any(l) else -1))
