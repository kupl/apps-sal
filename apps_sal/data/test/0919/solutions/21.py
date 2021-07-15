import math

n, k = list(map(int, input().split()))
str = input()
l = []
for elem in str:
    l.append(elem)
l.sort()
stup = chr(97-2)
x = 0
xc = 0
flag = True
for i in range(n):
    if ord(stup)+1 < ord(l[i]):
        x+=1
        xc += ord(l[i]) - 96
        stup = l[i]
        if x == k:
            print(xc)
            flag = False
            break
if flag:
    print(-1)








