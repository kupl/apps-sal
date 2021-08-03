n, m = map(int, input().split())
s = {}
for i in range(m):
    stemp = input().split()
    s[stemp[0]] = stemp[1]
    s[stemp[1]] = stemp[0]
st = input().split()
for i in range(len(st)):
    if(i == len(st) - 1):
        if(len(s[st[i]]) >= len(st[i])):
            print(st[i])
        else:
            print(s[st[i]])
    else:
        if(len(s[st[i]]) >= len(st[i])):
            print(st[i], end=' ')
        else:
            print(s[st[i]], end=' ')
