3
n = int(input())
A = list(map(int, input().split()))
mn = min(A)
mx = max(A)
ans = 0
for x in A:
    if mn < x < mx:
        ans += 1
print(ans)
