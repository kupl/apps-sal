n = int(input())
a = [int(s) for s in input().split()]
a.append(-1)
mx = max(a)
ans = 1
k = 0
for i in range(n + 1):
    if a[i] == mx:
        k += 1
    else:
        ans = max(ans, k)
        k = 0
print(ans)
