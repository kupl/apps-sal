n, size = map(int, input().split())
queue = []
head, tail = 0, 0

for i in range(n):
    time, during = map(int, input().split())
    while head != tail and time >= queue[head]:
        head += 1
    if tail - head - 1 < size:
        if head == tail:
            queue.append(time + during)
        else:
            queue.append(queue[-1] + during)
        print(queue[-1], end = ' ')
        tail += 1
    else:
        print('-1', end = ' ')
