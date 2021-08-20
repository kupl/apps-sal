import sys
import re


def mentioned_usernames(line):
    return {x for x in re.split('[^A-Za-z0-9]+', line)}


t = int(input())
for ti in range(t):
    possible_users = []
    messages = []
    n = int(input())
    usernames = set(input().split())
    m = int(input())
    for i in range(m):
        (user, text) = input().split(':')
        messages.append(text)
        if user == '?':
            mu = mentioned_usernames(text)
            possible_users.append(usernames - mentioned_usernames(text))
        else:
            possible_users.append({user})
    is_fixed = [False] * m
    for i in range(m - 1):
        if len(possible_users[i]) == 1:
            possible_users[i + 1].difference_update(possible_users[i])
            is_fixed = True
    for i in range(m - 1, 0, -1):
        if len(possible_users[i]) == 1:
            possible_users[i - 1].difference_update(possible_users[i])
            is_fixed = True
    res = []
    is_possible = True
    prev_user = '$'
    for i in range(m):
        if possible_users[i]:
            pusers = possible_users[i] - {prev_user}
            resx = next(iter(pusers))
            res.append(resx)
            prev_user = resx
        else:
            is_possible = False
            break
    if is_possible:
        for i in range(m):
            print('{}:{}'.format(res[i], messages[i]))
    else:
        print('Impossible')
