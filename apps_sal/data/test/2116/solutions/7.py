from sys import stdin, stdout
from collections import deque
numbers, everyq, allq = map(int, stdin.readline().split())
items = deque(list(map(int, stdin.readline().split())))
cnt = 0
for i in range(numbers):
    current = map(int, stdin.readline().split())
    for n in current:
        ind = 0
        while items[ind] != n:
            ind += 1
        cnt += ind + 1
        value = items[ind]
        for j in range(ind, 0, -1):
            items[j] = items[j - 1]
        items[0] = value

stdout.write(str(cnt))
