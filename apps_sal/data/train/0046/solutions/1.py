from collections import Counter


T = int(input())

for t in range(T):
    s = input()
    cc = Counter(s)
    fl = cc.most_common()[0][0]
    if fl == 'R':
        choice = 'P'
    elif fl == 'S':
        choice = 'R'
    else:
        choice = 'S'
    print(choice * len(s))
