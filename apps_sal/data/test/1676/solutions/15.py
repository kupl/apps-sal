from collections import deque
n, d = map(int, (input().split()))
per = input().split()
t = int(per[0]) + int(per[1])
per = 0
print(t, end=' ')
answer = t
queue = deque()
for i in range(n - 1):
    per1, per2 = map(int, input().split())

    while t < per1:
        if per >= 1:
            s = queue.pop()

            t += s
            per -= 1
        else:
            t = per1
            answer = t
    if t == per1:
        if per >= 1:
            s = queue.pop()

            per -= 1
            t += s
            if per < d:
                answer += per2
                print(answer, end=' ')
                queue.appendleft(per2)
                per += 1

        else:
            answer = answer + per2
            print(answer, end=' ')
            queue.appendleft(per2)

            per = 1

    else:
        if per < d:
            answer = answer + per2
            queue.appendleft(per2)
            print(answer, end=' ')
            per += 1
        else:
            print(-1, end=' ')
