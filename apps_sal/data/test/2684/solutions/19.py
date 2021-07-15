N = int(input())
st = input()
n = len(st)
a = []
mx = []
ans = False
for i in range(n):
    for j in range(i+1,n+1):
        if st[i:j] not in a:
            a.append(st[i:j])
for i in a:
    for j in range(len(i)//2):
        if i[j]==i[-1-j]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        mx.append(i)
m = max(mx, key=len)
print(len(m))
print(m)
            

