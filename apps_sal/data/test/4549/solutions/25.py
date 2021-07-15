h,w = map(int, input().split())
s = list()
t = list()
a = [0 for i in range(w+2)]
s.append(a)
for i in range(h):
    b = str(input())
    c = list(('0'+b+'0').replace('.','0').replace('#','1'))
    d = list(map(int, c))
    s.append(d)
    t.append(b)
s.append(a)
flag = 0

for j in range(1,h+1):
    for k in range(1,w+1):
        if flag == 1:
            break
        if s[j][k] == 1:
            cnt = 0
            cnt = s[j-1][k] + s[j][k-1] + s[j][k+1] + s[j+1][k] 
            if cnt == 0:
                flag = 1
                print('No')

if flag == 0:
    print('Yes')
