from collections import deque
N = int(input())
P = list(map(int, input().split()))
if P == list(range(2, N + 1)) + [1]:
    print(*list(range(N - 1, 0, -1)), sep='\n')
    return
ans = []
d = deque([(0, N - 1)])
while len(d):
    left, right = d.popleft()
    n = right - left + 1
    if n == 1:
        continue
    if n == 2:
        if P[left] == left + 1 and P[right] == right + 1:
            print(-1)
            break
        ans.append(left + 1)
        continue
    min_a = 10**7
    max_a = -1
    for i in range(n - 1):
        if min(min_a, P[left + i + 1]) == left + 1 and max(max_a, P[left + i + 1]) == left + 1 + i:
            P[left + i], P[left + i + 1] = P[left + i + 1], P[left + i]
            d.append((left, left + i))
            d.append((left + i + 1, right))
            ans.append(left + i + 1)
            break
        min_a = min(min_a, P[left + i])
        max_a = max(max_a, P[left + i])
    else:
        print(-1)
        break
else:
    print(*ans, sep='\n')
