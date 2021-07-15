from collections import deque

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

a = deque(A)

arrival = 1
ans = 0

while arrival < N:
    score = a.popleft()
    if arrival == 1:
        ans += score
        arrival += 1
    else:
        ans += score*min(2, N - arrival)
        arrival += 2

print(ans)
