n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
r = a[-1]
for i in range(1,r+1):
    if r%i==0:
        a.remove(i)
a = sorted(a)
t = a[-1]
print(r,t)

