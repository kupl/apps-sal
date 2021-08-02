n = int(input())
cnt = 1
ans = 0
l = list()
for i in range(2 * n):
    s = input()
    if(s[0] == 'a'):
        l.append(int(s[4:]))
    else:
        if(len(l) == 0):
            pass
        elif(l[-1] == cnt):
            l.pop()
        else:
            ans += 1
            l = list()
        cnt += 1
print(ans)
