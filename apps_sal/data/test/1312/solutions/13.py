n, k = map(int,input().split())
res = [n//k for i in range(k)]
for i in range(n%k):
    res[i] += 1

for x in sorted(res): print(x,end=' ')
