import sys
input = sys.stdin.readline
N = int(input())
A = [[x - 1 for x in list(map(int, input().split()))] for _ in range(N)]


def can_match(i, A, next_set):
    if not A[i]:
        return
    j = A[i][0]
    if A[j][0] == i:
        if i < j:
            next_set.add((i, j))
        else:
            next_set.add((j, i))


next_set = set()
for i in range(N):
    can_match(i, A, next_set)
day = 0
battle = 0
while next_set:
    day += 1
    (current_set, next_set) = (next_set, set())
    for match in current_set:
        battle += 1
        del A[match[0]][0]
        can_match(match[0], A, next_set)
        del A[match[1]][0]
        can_match(match[1], A, next_set)
if battle == N * (N - 1) // 2:
    print(day)
else:
    print(-1)
