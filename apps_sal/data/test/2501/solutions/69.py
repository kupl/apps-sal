import collections

N = int(input())
A = list(map(int, input().split()))

# ap+aq == p-q (p>q)
# p-ap = q+aq

mp = {}
ans = 0
for p in range(N):
    if p-A[p]+1 in mp:
        ans += mp[p-A[p]+1]
    if p+A[p]+1 in mp:
        mp[p+A[p]+1] += 1
    else:
        mp[p + A[p] + 1] = 1

print(ans)



