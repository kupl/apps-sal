3

import re

t = int(input())

for ti in range(t):
    n = int(input())
    users = set(input().split(' '))

    m = int(input())
    messages = []

    guessed = [None for i in range(m)]
    denied = [set() for i in range(m)]

    for i in range(m):
        mg = input()
        if not mg.startswith('?:'):
            guessed[i] = mg[:mg.find(':')]

        mg = mg[mg.find(':'):]
        messages.append(mg)

        m2 = mg + ' '
        for u in users:
            if re.search('[^a-zA-Z0-9]' + u + '[^a-zA-Z0-9]', m2):
                denied[i].add(u)

    answer = True

    for i in range(m):
        if guessed[i]:
            if i > 0: denied[i-1].add(guessed[i])
            if i < m-1: denied[i+1].add(guessed[i])

    for i in range(m):
        if guessed[i] in denied[i]:
            answer = False

    #print(guessed)
    #print(denied)

    changed = True
    while changed and answer:
        changed = False
        for i in range(m):
            if not guessed[i]:
                if len(users) - len(denied[i]) == 1:
                    changed = True
                    guessed[i] = (users - denied[i]).pop()
                    if i > 0: denied[i-1].add(guessed[i])
                    if i < m-1: denied[i+1].add(guessed[i])
                if len(users) == len(denied[i]):
                    answer = False
                    break

    for i in range(m):
        if not guessed[i] and len(users) - len(denied[i]) >= 1:
            guessed[i] = (users - denied[i]).pop()
            if i < m-1: denied[i+1].add(guessed[i])


    for i in guessed:
        if not i:
            answer = False

    if not answer:
        print("Impossible")
    else:
        for i in range(m):
            print(guessed[i] + messages[i])
    

