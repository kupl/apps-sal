from sys import stdin, stdout
n,k,p = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(x) for x in stdin.readline().rstrip().split()]
a = sorted(a)
b = [int(x) for x in stdin.readline().rstrip().split()]
b = sorted(b)

ans = int(2e9+1)
for i in range(k-n+1):
    tmp = 0
    for j in range(n):
        tmp = max(tmp,abs(a[j]-b[j+i])+abs(b[j+i]-p))
    ans = min(ans,tmp)
print(ans)
