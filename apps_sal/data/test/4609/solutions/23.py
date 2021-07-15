import collections 
N = int(input())
lsA = []
for i in range(N):
    lsA.append(int(input()))
counterA = collections.Counter(lsA)
ans = 0
for i in counterA.values():
    ans += i%2
print(ans)
