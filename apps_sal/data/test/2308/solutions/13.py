from sys import stdin
input=stdin.readline
for i in range(int(input())):
    x=input()[::-1]
    y=input()[::-1]
    k=0
    for i in range(len(y)):
        if y[i]=='1':
            break
    while i<len(x):
        if x[i]=='1':
            break
        i+=1
        k+=1
    print(k)

