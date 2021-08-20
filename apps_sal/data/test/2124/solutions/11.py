import re


def add_used(id, s, used):
    used[id - 1].add(s)
    used[id].add(s)
    used[id + 1].add(s)


tcase = int(input())
for cas in range(tcase):
    n = int(input())
    names = input().split()
    m = int(input())
    res = True
    ans = [''] * (m + 1)
    msg = [''] * (m + 1)
    used = [set() for i in range(m + 1)]
    for i in range(m):
        (ans[i], msg[i]) = input().split(':')
        if ans[i] != '?':
            add_used(i, ans[i], used)
        mentioned = re.split('\\W+', msg[i])
        for s in mentioned:
            if s in names:
                used[i].add(s)
    for i in range(m):
        if ans[i] == '?' and len(used[i]) == n - 1:
            ans[i] = list(set(names) - used[i])[0]
            add_used(i, ans[i], used)
    for i in range(m):
        if ans[i] == '?':
            if len(used[i]) == n:
                res = False
            else:
                ans[i] = list(set(names) - used[i])[0]
                add_used(i, ans[i], used)
    for i in range(m - 1):
        if ans[i] == ans[i + 1]:
            res = False
    if res:
        for i in range(m):
            print(ans[i] + ':' + msg[i])
    else:
        print('Impossible')
