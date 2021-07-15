n = int(input())
a = list(map(int,input().split()))
a.sort()
c = 0
while sum(a)/len(a) < 4.5:
    a[a.index(min(a))] = 5
    c+=1
print(c)

