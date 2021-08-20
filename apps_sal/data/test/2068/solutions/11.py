import sys


def add_user(d, u):
    if u in d:
        return d[u]
    else:
        d[u] = len(d)
        return d[u]


n = int(input())
who = [[] for i in range(n + 1)]
users = {}
answer_id = -1
for i in range(n):
    str = input()
    parts = str.split(' ')
    name_one = parts[0].lower()
    name_two = parts[2].lower()
    user_one = add_user(users, name_one)
    user_two = add_user(users, name_two)
    who[user_two].append(user_one)
    if name_two == 'polycarp':
        answer_id = user_two


def dfs(u):
    res = 1
    for v in who[u]:
        res = max(res, dfs(v) + 1)
    return res


print(dfs(answer_id))
