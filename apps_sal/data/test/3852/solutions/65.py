from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      list(map(int, input().split()))
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = inl()
mx = max([abs(x) for x in a])
p = [i for i in range(n) if abs(a[i])==mx][0]
seq = []
if a[p]>0:
    for i in range(1,n):
        while a[i-1]>a[i]:
            a[i] += a[p]
            seq.append((p,i))
        if a[i]>a[p]:
            p = i
elif a[p]<0:
    for i in range(n-2,-1,-1):
        while a[i]>a[i+1]:
            a[i] += a[p]
            seq.append((p,i))
        if a[i]<a[p]:
            p = i
print((len(seq)))
for a,b in seq:
    print(("{} {}".format(a+1,b+1)))

