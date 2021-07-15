n = int(input())
a = list(map(int, input().split()))
mx = -1
ans = -1
for i in range(n):
    if a[i] > mx+1:
        ans = i+1
        break
    else:
        mx = max(mx, a[i])
print(ans)
