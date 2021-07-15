import bisect
a=[3,5,7]
c=[3,5,7]
for i in range(8):
    b=[]
    for j in a:
        for k in range(3):
            b.append(int(str(j)+str(k*2+3)))
            c.append(int(str(j)+str(k*2+3)))
    a=b
n=int(input())
def is755(d):
    if len(set(list(str(d))))<3:
        return False
    else:
        return True
print(sum([i<=n and is755(i) for i in c]))
