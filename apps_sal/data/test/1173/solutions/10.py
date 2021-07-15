from collections import deque
N = int(input())
A = [deque(map(lambda x: int(x)-1,input().split(" "))) for _ in range(N)]
ans = 0
used_prev = set(range(N))

while any(A):
    used = set()
    for i in used_prev:
        a = A[i]
        if not a or i in used:
            continue
        j = a[0]
        b = A[j]
        if not b or j in used:
            continue
        if i == b[0]:
            A[i].popleft()
            A[j].popleft()
            used.add(i)
            used.add(j)
    if not used:
        ans = -1
        break
    used_prev = used
    ans += 1
print(ans)
