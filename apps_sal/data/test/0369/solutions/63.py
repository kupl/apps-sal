import bisect
safe = []
n, m = map(int, input().split())
field = list(input())
for i in range(n + 1):
    if field[i] == "0":
        safe.append(i)
start = n


deque = []
flag = True
while start > 0:
    if start >= m:
        index = bisect.bisect_left(safe, start - m)
        if safe[index] != start:
            deque.append(start - safe[index])
            start = safe[index]

        elif safe[index] == start:
            flag = False
            start = 0
    else:
        deque.append(start)
        start = 0
if flag:
    deque = deque[::-1]
    print(*deque)
else:
    print(-1)
