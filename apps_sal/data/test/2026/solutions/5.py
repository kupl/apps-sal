n = int(input())
s = input()
cur = 0
su = 0
while(cur != n):
    q = set()
    flag = 0
    while(cur != n and flag == 0):
        if(s[cur] == 'R' and 'L' not in q):
            q.add('R')
            cur += 1
        elif(s[cur] == 'L' and 'R' not in q):
            q.add('L')
            cur += 1
        elif(s[cur] == 'U' and 'D' not in q):
            q.add('U')
            cur += 1
        elif(s[cur] == 'D' and 'U' not in q):
            q.add('D')
            cur += 1
        else:
            flag = 1
        if(cur == n):
            flag = 1
    su += 1
print(su)
