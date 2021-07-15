from collections import defaultdict
n,m = map(int,input().split())
a = [int(i) for i in input().split()]
s = [0]*(n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]
dct = defaultdict(int)
for i in range(n+1):
    dct[s[i]%m] += 1
ans = 0
for v in dct.values():
    ans += v*(v-1)//2
print(ans)
