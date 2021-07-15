from collections import defaultdict
n1, n2 = input(), input()
n = int(input())
#mp = defaultdict(list)
mp = [[0 for i in range(100)], [0 for i in range(100)]]

for i in range(n):
    line = input().split()
    t = int(line[0])
    m = int(line[2])
    if line[1] == 'h':
        mp[0][m] += 1
        if line[3] == 'r':
            
            if mp[0][m] < 3:
                print(n1, m, t)
            mp[0][m] = 3
            continue
        if mp[0][m] == 2:
            print(n1, m, t)
            mp[0][m] = 3
    else:
        mp[1][m] += 1
        if line[3] == 'r':
            if mp[1][m] < 3:
                print(n2, m, t)
            mp[1][m] = 3
            continue
        if mp[1][m] == 2:
            print(n2, m, t)
            mp[1][m] = 3

