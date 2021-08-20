n = int(input())
for i in range(n):
    k = int(input())
    cnt = 0
    bad = []
    s = input()
    t = input()
    for i in range(k):
        if s[i] != t[i]:
            cnt += 1
            bad.append(i)
    if cnt != 2:
        print('No')
    elif s[bad[0]] != s[bad[1]] or t[bad[0]] != t[bad[1]]:
        print('No')
    else:
        print('Yes')
