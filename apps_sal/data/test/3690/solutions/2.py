from sys import stdin, stdout

h, m, s, t1, t2 = list(map(int,stdin.readline().rstrip().split()))

h+=0.1
m+=0.1

if t1>t2:
    t1,t2 = t2,t1

betweenCount = 0
if h<t2 and h>t1:
    betweenCount+=1
if m<t2*5 and m>t1*5:
    betweenCount+=1
if s<t2*5 and s>t1*5:
    betweenCount+=1

if betweenCount==3 or betweenCount==0:
    print("YES")
else:
    print("NO")

