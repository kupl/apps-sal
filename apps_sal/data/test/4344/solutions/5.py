n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * 101
q = 0
ans = []
for i in range(n):
    if b[a[i]] == 0:
        b[a[i]] = 1
        q += 1
        if (q <= k):
            ans.append(i + 1)
if q >= k:
    print("YES") 
    print(*ans)
else:
    print("NO")
