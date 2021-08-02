from collections import deque
N = int(input())
A = [list([int(x) - 1 for x in input().split()])[::-1] for _ in range(N)]
q = deque([])

# 選手iが試合ができるかをチェックして、できるならばキューに入れる


def check(i, q):
    if len(A[i]) == 0:
        return
    j = A[i][-1]
    if len(A[j]) == 0:
        return
    if A[j][-1] == i:
        if i > j:
            i, j = j, i
        q.append((i, j))
    return


for i in range(N):
    check(i, q)

day = 0
while q:
    day += 1
    q = set(sorted(q))
    prev = deque([])
    prev, q = q, prev
    for i, j in prev:
        A[i].pop(-1)
        A[j].pop(-1)
    for i, j in prev:
        check(i, q)
        check(j, q)

for i in range(N):
    if len(A[i]) != 0:
        print((-1))
        return

print(day)
