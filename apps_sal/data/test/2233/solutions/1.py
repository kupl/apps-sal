q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    t = input()
    cnt = 0
    tmp = []
    for i in range(n):
        if s[i] != t[i]:
            cnt += 1
            tmp.append(i)
    if cnt == 0:
        print('Yes')
    elif cnt == 1:
        print('No')
    elif cnt == 2:
        if s[tmp[0]] == s[tmp[1]] and t[tmp[0]] == t[tmp[1]]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
