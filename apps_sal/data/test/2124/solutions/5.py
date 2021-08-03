def dfs(ind):
    if ind > 0:
        if possible[ind][0] in possible[ind - 1]:
            possible[ind - 1].remove(possible[ind][0])
            if len(possible[ind - 1]) == 1:
                dfs(ind - 1)
    if ind < m - 1:
        if possible[ind][0] in possible[ind + 1]:
            possible[ind + 1].remove(possible[ind][0])
            if len(possible[ind + 1]) == 1:
                dfs(ind + 1)


def Check(st, ms):
    for i in range(0, len(ms) - len(st) + 1):
        if st == ms[i:i + len(st)]:
            t = True
            if i > 0:
                if ms[i - 1] == ' ' or ms[i - 1] == '.' or ms[i - 1] == ',' or ms[i - 1] == '?' or ms[i - 1] == '!':
                    e = 0
                else:
                    t = False
            if i < len(ms) - len(st):
                if (ms[i + len(st)] == ' ' or ms[i + len(st)] == '.' or ms[i + len(st)] == ',' or ms[i + len(st)] == '?' or ms[i + len(st)] == '!'):
                    e = 0
                else:
                    t = False
            if t:
                return True
    return False


def R(): return list(map(int, input().split(' ')))


#r, w = open("input.txt", "r"), open("output.txt", "w")
T = int(input())
while T:
    n = int(input())
    users = input().split(' ')
    m = int(input())
    possible = [[] for i in range(m)]
    sender, message = [], []
    for i in range(m):
        s = input().split(':')
        sender.append(s[0])
        message.append(s[1])
    for i in range(m):
        if sender[i] == '?':
            unallow = " "
            if i > 0 and len(possible[i - 1]) == 1:
                unallow = possible[i - 1][0]
            for j in users:
                if j == unallow:
                    continue
                done = Check(j, message[i])
                if not done:
                    possible[i].append(j)
        else:
            possible[i].append(sender[i])
    used = [0 for i in range(m)]
    for i in range(m):
        if len(possible[i]) == 1 and used[i] == 0:
            dfs(i)
    for i in range(m):
        if len(possible[i]) > 1:
            possible[i] = [possible[i][0]]
            dfs(i)
    done = False
    for i in possible:
        if len(i) == 0:
            print("Impossible")
            done = True
            break
    if not done:
        for i in range(m):
            print(possible[i][0] + ':' + message[i])
    T -= 1
