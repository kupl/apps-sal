n = int(input())
s = []
for i in range(n):
    s.append(input().split())
    if s[i][0] > s[i][1]:
        s[i][0], s[i][1] = s[i][1], s[i][0];
x = [int(i) - 1 for i in input().split()]

tag = False
#for item in s:
#    print(item)
for i in range(1, n):
    if s[x[i-1]][0] >= s[x[i]][1]:
        print('NO')
        tag = True
        break
    if s[x[i-1]][0] >= s[x[i]][0]:
        s[x[i]][0] = s[x[i]][1]
    #print(s[i][0])
if tag == False:
    print('YES')

