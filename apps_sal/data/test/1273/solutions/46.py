from bisect import insort
from collections import deque
N = int(input())
inp = []
for k in range(N - 1):
    (a, b) = map(int, input().split())
    if a > b:
        (a, b) = (b - 1, a - 1)
    else:
        (a, b) = (a - 1, b - 1)
    inp.append((a, b, k))
inp.sort(key=lambda x: x[0])
inp = deque(inp)
mark = [[] for _ in range(N)]


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False


ans = [0 for _ in range(N - 1)]
now = 0
cnt = 0
while inp:
    item = inp.popleft()
    cnt += 1
    if now < item[0]:
        now = item[0]
        cnt = 1
    while binary_search(mark[item[0]], cnt) or binary_search(mark[item[1]], cnt):
        cnt += 1
    insort(mark[item[1]], cnt)
    ans[item[2]] = cnt
color = max(ans)
print(color)
for k in range(N - 1):
    print(ans[k])
