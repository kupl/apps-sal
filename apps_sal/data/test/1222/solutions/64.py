from collections import deque
k = int(input())
d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while d:
    now = d.popleft()
    hitoketa = now % 10
    for i in [-1, 0, 1]:
        if 0 <= hitoketa + i <= 9:
            nxt = now * 10 + hitoketa + i
            if nxt <= 3234566667:
                num.append(nxt)
                d.append(nxt)
num.sort()
print((num[k - 1]))
