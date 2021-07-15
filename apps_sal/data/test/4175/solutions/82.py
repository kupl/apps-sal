n=int(input())
w=[""]*n
a=set()
for i in range(n):
    w[i]=input()
cnt=0
for x in w:
    if x in a:
        print("No")
        return
    else:
        if cnt>0:
            if bef!=x[0]:
                print("No")
                return
        bef=x[-1]
    cnt+=1
    a.add(x)
print("Yes")

