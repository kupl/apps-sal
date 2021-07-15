n = int(input())
b = list(map(int,input().split()))
ans = 0
aa = 0
ab = 100001
for i in range(n-1):
    aa = min(ab,b[i])
    ab = b[i]
    ans += aa
print(ans+ab)
