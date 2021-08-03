n = int(input())
a = list(map(int, input().split()))
mn = min(a)
mx = max(a)
ans = 0
for x in a:
    if x > mn and x < mx:
        ans += 1
print(ans)
