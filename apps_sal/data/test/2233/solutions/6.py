k = int(input())
for nt in range(k):
    n = int(input())
    s = input()
    t = input()
    diff = 0
    same = 0
    d = []
    for i in range(n):
        if s[i] == t[i]:
            same += 1
        else:
            diff += 1
            d.append([s[i], t[i]])
    if diff > 2:
        print('No')
    elif diff == 1:
        print('No')
    elif diff == 0:
        print('Yes')
    elif d[0][0] == d[1][0] and d[0][1] == d[1][1]:
        print('Yes')
    else:
        print('No')
