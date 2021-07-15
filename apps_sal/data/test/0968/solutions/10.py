'''
Created on Sep 28, 2014

@author: Ismael
'''

def selectLeastGreater(p,prec):
    fn = p[0]
    ln = p[1]
    if(fn >= prec and fn <= ln):
        return fn
    elif(ln >= prec and ln <= fn):
        return ln
    elif(fn >= prec):
        return fn
    elif(ln >= prec):
        return ln
    else:
        return ""

n = int(input())
names = []
for _ in range(n):
    fn,ln = input().split()
    names.append((fn,ln))
A = list(map(int,input().split()))
#print(names)
#print(A)
names2 = []
for i in A:
    names2.append(names[i-1])
#print(names2)
prec = ""
YES = True
for i in range(n):
    new = selectLeastGreater(names2[i],prec)
    if(len(new) == 0):
        print("NO")
        YES = False
        break
    else:
        prec = new
if(YES):
    print("YES")
