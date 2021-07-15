n = int(input())
w = list(map(int,input().split()))
wa = sum(w)
ans = float('inf')
for i in range(1,n):
    s1 = sum(w[:i])
    s2 = wa - s1
    ans = min(ans, abs(s1-s2))
print(ans)
