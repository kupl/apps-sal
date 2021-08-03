n = int(input())
ct = [0] * n
mx = [0] * n
for i in range(n):
    a = list(map(int, input().split()))
    ct[i] = a[0]
    mx[i] = max(a[1:])
ans = 0
rf = max(mx)
for i in range(n):
    ans = ans + (rf - mx[i]) * ct[i]
print(ans)
