from collections import deque


def is_not_empty(A):
    for x in A:
        if x:
            return True
    return False


N = int(input())
A = [deque([int(i) - 1 for i in input().split()]) for _ in range(N)]
ans = 0
yesterday = set(range(N))
while is_not_empty(A):
    today = set()
    for my in yesterday:
        if not A[my]:
            continue
        if my in today:
            continue
        enemy = A[my][0]
        if my == A[enemy][0] and enemy not in today:
            today.add(A[my].popleft())
            today.add(A[enemy].popleft())
    if not today:
        ans = -1
        break
    ans += 1
    yesterday = today
print(ans)
