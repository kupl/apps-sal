I = lambda : map(int,input().split())
n = int(input())
#li = list(I())
if n == 1 or n==2 :
    print("YES");return
if n==3 :
    print("NO");return
lii = [ [] for i in range (n+1)]
for i in range (n-1) :
    x , y = I()
    lii[x] += [y]
    lii[y] += [x]
pp = 0 
for i in range (1,n+1) :
    if len(lii[i]) == 1 :
        continue
    elif len(lii[i]) == 2 :
        pp = 1
        break
if pp == 1 :
    print("NO");return
print("YES");return        
