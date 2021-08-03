from queue import Queue
stack = Queue()

n, k = list(map(int, input().split()))
s = list(input())

k -= 1
a = set()
answer = 0

stack.put(list(s))

while not stack.empty():
    now = stack.get_nowait()
    new = now[:]
    can = []
    for i in range(len(now)):
        if k:
            new[i] = ''
            word = ''.join(new)
            if word not in a:
                a.add(word)
                answer += n - len(word)
                can.append(word)
                k -= 1

        new[i] = now[i]
    if k:
        for word in can:
            stack.put(list(word))

if k > 0:
    print(-1)
else:
    print(answer)
