from bisect import bisect_right
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [a[0]]
for ai in a[1:]:
    s.append(s[-1] + ai)

ans = 0
for i in range(n):
    if s[i] >= k:
        d = s[i]-k
        ans += bisect_right(s, d)+1
print(ans)

