n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    a[i] -= (i+1)

a.sort()

m = a[n//2]
ans = 0
for i in range(n):
    ans += abs(a[i]-m)

print(ans)
