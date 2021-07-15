import sys
n,m = list(map(int, input().split()))
s = [input() for i in range(n)]
d=list([int(x)-1 for x in input().split()])
ans =  list(s[d[0]]);
for i in range(1,m):
    if len(s[d[i]]) != len(ans):
        print("No")
        return
    for o in range(0, max([len(ans), len(s[d[i]])])):
       if ans[o] != '?' and ans[o] != s[d[i]][o]:
            ans[o] = '?'
f = True
for i in range(0,n):
    if len(ans) != len(s[i]):
        continue
    if i in d:
        continue
    f = True
    for o in range(0,len(ans)):
        if ans[o] != '?' and ans[o] != s[i][o]:
            f = False
            break
    if f:
        print("No")
        return
print("Yes")
print(''.join(ans))


