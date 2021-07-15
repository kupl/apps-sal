N = int(input())
st = input()
n = len(st)
a = set()
mx =[]
ans = False
for i in range(n):
    for j in range(i+1,n+1):
        a.add(st[i:j])
a = list(a)
for i in a:
    for j in range(len(i)//2):
        if i[j]==i[-1-j]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        mx.append(i)
    else:
        continue
m = max(mx, key=len)
print(len(m))
print(m)
            

