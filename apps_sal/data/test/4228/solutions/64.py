N, L = list(map(int, input().split()))

ans = 0
for i in range(1, N+1):
    ans += L+i-1
    

if L+N-1 < 0:
    ans -= (L+N-1)
elif L <= 0 <= L+N-1:
    ans = ans
else:
    ans -= L
print(ans)

