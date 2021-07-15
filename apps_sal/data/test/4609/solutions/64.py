import collections
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
    
cnt = collections.Counter(A)
ans = 0
for v in cnt.values():
    if v % 2 != 0:
        ans += 1
        
print(ans)
