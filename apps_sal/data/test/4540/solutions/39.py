n = int(input())
a = list(map(int, input().split()))
a.append(0)
a.insert(0,0)
s = 0
for i in range(len(a)-1):
    s += abs(a[i]-a[i+1])
for h in range(1,n+1):
    t = abs(a[h+1]-a[h-1])-abs(a[h]-a[h-1])-abs(a[h+1]-a[h])
    print(s+t)
