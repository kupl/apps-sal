import queue
t = int(input())
for i in range(t):
    n = int(input())
    q = queue.Queue()
    answer = []
    current_sec = 1
    for j in range(n):
        s = input().split(' ')
        l = int(s[0])
        r = int(s[1])
        while l > current_sec:
            if not q.empty():
                time = q.get()
                if time >= current_sec:
                    answer.append(str(current_sec))
                    current_sec += 1
                else:
                    answer.append('0')
            else:
                current_sec = l
        if l == current_sec:
            q.put(r)
    while not q.empty():
        time = q.get()
        if time >= current_sec:
            answer.append(str(current_sec))
            current_sec += 1
        else:
            answer.append('0')
    res = ' '.join(answer)
    print(res)
