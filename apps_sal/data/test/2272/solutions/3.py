data = []
for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        data.append(cmd[1:])
    else:
        done = [False] * (len(data) + 1)
        que = [cmd[1] - 1]
        while len(que):
            p = que[0]
            del que[0]
            for (i, v) in enumerate(data):
                if (v[0] < data[p][0] < v[1] or v[0] < data[p][1] < v[1]) and (not done[i]):
                    done[i] = True
                    que.append(i)
        print('YES' if done[cmd[2] - 1] else 'NO')
