from sys import stdin, exit


def listInput():
    return list(map(int, stdin.readline().rstrip().split()))


n, x = listInput()
li = listInput()
dic1 = {}
#print('x is ',x)
for i in li:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1
dic2 = {}
for i in li:
    #print('for ',i,' &x is ',i&x)
    if i & x in dic2:
        dic2[i & x] += 1
    else:
        dic2[i & x] = 1
ans = n + 1
# rint(dic1)
# print(dic2)
for i in li:
    if dic1[i] >= 2:
        ans = min(ans, 0)
    elif i != (i & x) and (i & x) in dic1:
        ans = min(ans, 1)
    elif (i & x) in dic1 and dic1[i & x] >= 2:
        ans = min(ans, 1)
    elif i != (i & x) and i in dic2:
        ans = min(ans, 1)
    elif (i & x) in dic2 and dic2[i & x] >= 2:
        ans = min(ans, 2)

if ans == (n + 1):
    print(-1)
else:
    print(ans)
