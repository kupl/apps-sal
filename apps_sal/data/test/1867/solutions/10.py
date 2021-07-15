def bin_search(n,a):
    l = 0
    r = len(a)-1
    while l<=r:
        m = (l+r)//2
        if n>a[m][0]:
            l = m+1
        if n<a[m][0]:
            r = m-1
        if n == a[m][0]:
            return m
    return -1
n = int(input())
a = input().split()
def ke(n):
    return n[1]
def f(n):
    return abs(n[2]-n[3])
cnt = {}
mx = 0
for i in range(n):
    a[i] = int(a[i])
    if a[i] in cnt:
        cnt[a[i]][1] += 1
        cnt[a[i]][3] = i
    else:
        cnt[a[i]] = [a[i],1,i,0]
for m in list(cnt.values()):
    if m[1]>mx:
        mx = m[1]
v = []
for m in list(cnt.values()):
    if m[1]==mx:
        v.append(m)
v.sort(key=f)
print(v[0][2]+1,v[0][3]+1)

