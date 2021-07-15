n=int(input())
a = list(map(int,input().split()))
_sum =sum(a) / n
s  = round(_sum)
ans = 0
#print(s)
for i in range(n):
    v =(a[i]-s)**2
    ans += v
print(ans)
