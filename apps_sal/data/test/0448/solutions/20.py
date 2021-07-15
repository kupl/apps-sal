from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = deque()
for i in range(n):
    pairs.append([arr[i], (i + 1)])
while len(pairs) > 1:
    pairs[0][0] -= m
    if pairs[0][0] > 0:
        pairs.append(pairs[0])
    pairs.popleft()
print(pairs[0][1])
