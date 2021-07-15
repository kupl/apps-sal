n, m, k = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
lis = []
for i in range(1,len(b)):
    lis.append(b[i]-b[i-1]-1)
lis.sort()
ans = n
for i in range(n-k):
    ans += lis[i]
print(ans)

