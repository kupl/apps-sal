import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for a in range(1, n-1):
    for b in range(a+1, n):
        ans += max(0, a-bisect.bisect(l, l[b]-l[a]))                                       
print(ans)
