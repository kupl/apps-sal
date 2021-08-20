from collections import deque
from bisect import bisect_left
N = int(input())
P = list(map(int, input().split()))
big = []
for k in range(N):
    big.append((P[k], k + 1))
big.sort(key=lambda x: x[0], reverse=True)
big = deque(big)
item = big.popleft()
done = [0, 0, item[1], N + 1, N + 1]
ans = 0
while big:
    item = big.popleft()
    index = item[1]
    num = item[0]
    i = bisect_left(done, index)
    done.insert(i, index)
    ans += num * ((done[i + 2] - done[i + 1]) * (index - done[i - 1]) + (done[i - 1] - done[i - 2]) * (done[i + 1] - index))
print(ans)
