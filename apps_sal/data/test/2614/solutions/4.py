from sys import stdin
from collections import deque
import heapq
tt = int(stdin.readline())
for loop in range(tt):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dic = {}
    for i in a:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    l = 0
    r = n
    while r - l != 1:
        m = (l + r) // 2
        q = []
        wait = deque([])
        for i in dic:
            heapq.heappush(q, (-1 * dic[i], i))
        flag = True
        for i in range(n):
            while len(wait) > 0 and wait[0][0] < i - m:
                (last, count, num) = wait.popleft()
                heapq.heappush(q, (count, num))
            if len(q) == 0:
                flag = False
                break
            (count, num) = heapq.heappop(q)
            count += 1
            if count != 0:
                wait.append((i, count, num))
        if flag:
            l = m
        else:
            r = m
    print(l)
