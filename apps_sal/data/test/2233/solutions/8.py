for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    x = []
    for i in range(n):
        if s[i] != t[i]:
            x.append(i)
    if len(x) != 2:
        print('No')
    elif s[x[0]] == s[x[1]] and t[x[0]] == t[x[1]]:
        print('Yes')
    else:
        print('No')
