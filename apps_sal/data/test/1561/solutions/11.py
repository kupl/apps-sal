s = input()
s = s.strip().split(' ')
n = int(s[0])
m = int(s[1])
k = int(s[2])

mp = []

for i in range(n):
    string = input()
    temp = []
    for j in range(m):
        temp.append(string[j])
    mp.append(temp)

ans = 0

for i in range(n):
    begin = 0
    while begin < m:
        # print (begin)
        if (mp[i][begin] == '.'):
            temp = begin
            while mp[i][temp] == '.':
                temp += 1
                if temp == m: break
            length = temp - begin
            begin = temp
            ans += max(0, length - k + 1)
        begin += 1

for i in range(m):
    begin = 0
    while begin < n:
        if (mp[begin][i] == '.'):
            temp = begin
            while mp[temp][i] == '.':
                temp += 1
                if temp == n: break
            length = temp - begin
            begin = temp
            ans += max(0, length - k + 1)
        begin += 1

if k == 1:
    ans = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] == '.':
                ans += 1


print(ans)
