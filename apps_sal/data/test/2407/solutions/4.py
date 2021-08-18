'''input
2
3 2
1 3 5
4 1
5 2 3 5
'''
from sys import stdin


q = int(stdin.readline().strip())
for _ in range(q):
    n, r = list(map(int, stdin.readline().split()))
    monsters = list(map(int, stdin.readline().split()))
    monsters.sort()
    monsters = list(set(monsters))

    impact = 0
    count = 0
    for i in range(len(monsters) - 1, -1, -1):
        if monsters[i] - impact <= 0:
            break
        else:
            impact += r
            count += 1

    print(count)
