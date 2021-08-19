(num, s) = map(int, input().split())
queue = input()
for i in range(s):
    new_queue = ''
    while len(queue) > 0:
        if queue[0] == 'G':
            new_queue += 'G'
            queue = queue[1:]
        elif len(queue) > 1 and queue[1] == 'G':
            new_queue += 'GB'
            queue = queue[2:]
        else:
            new_queue += 'B'
            queue = queue[1:]
    queue = new_queue
print(queue)
