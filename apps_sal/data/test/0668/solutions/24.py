def send(id):
    while a[id] > 0:
        if len(g) < n:
            li = a.copy()
            li[id] = -1
            while True:
                k = li.index(max(li))
                if k + 1 in g:
                    li[k] = -1
                else:
                    break
            g.append(k + 1)
            actions.append('{} {}'.format(id + 1, g[-1]))
            send(k)
            a[id] -= 1
        else:
            break


n = int(input())
a = list(map(int, input().split()))
actions = []
g = [1]
send(0)
if len(g) < n:
    print(-1)
else:
    print(len(actions))
    for line in actions:
        print(line)

