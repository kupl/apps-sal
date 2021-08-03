def main():
    n = int(input())
    names = input().split()
    m = int(input())
    msg = [input().split(':') for _ in range(m)]
    texts = []
    for i in msg:
        texts.append(i[1])
        i[1] = i[1].replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()
        if i[0] == '?':
            i.append([])
            for name in names:
                if name not in i[1]:
                    i[2].append(name)
            if len(i[2]) == 0:
                print('Impossible')
                return
    go_on = True
    while go_on:
        go_on = False
        for i in range(len(msg)):
            if msg[i][0] != '?':
                continue
            if i - 1 > -1 and msg[i - 1][0] in msg[i][2]:
                msg[i][2].remove(msg[i - 1][0])
                go_on = True
            if i + 1 < m and msg[i + 1][0] in msg[i][2]:
                msg[i][2].remove(msg[i + 1][0])
                go_on = True
            if len(msg[i][2]) == 0:
                print('Impossible')
                return
            if len(msg[i][2]) == 1:
                msg[i][0] = msg[i][2][0]
                del msg[i][2]
                go_on = True
    for i in range(len(msg)):
        if msg[i][0] == '?':
            msg[i][0] = msg[i][2][0]
            if i < m - 1 and len(msg[i + 1]) == 3 and msg[i][0] in msg[i + 1][2]:
                msg[i + 1][2].remove(msg[i][0])
        print(msg[i][0], ':', texts[i], sep='')


t = int(input())

for _ in range(t):
    main()
