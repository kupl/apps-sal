from collections import deque


def main():
    s = list(input())
    q = int(input())
    query = []
    que = deque(s)
    f = False
    for i in range(q):
        query.append(input().split(' '))
    for i in range(q):
        if query[i][0] == '1':
            f = not f
        elif f:
            if query[i][1] == '2':
                que.appendleft(query[i][2])
            else:
                que.append(query[i][2])
        elif query[i][1] == '1':
            que.appendleft(query[i][2])
        else:
            que.append(query[i][2])
    if f:
        que.reverse()
    print(''.join(que))


def __starting_point():
    main()


__starting_point()
