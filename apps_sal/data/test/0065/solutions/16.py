n = int(input())
a = list(map(int, input().split()))
m = min(a)
ans = 1000000000
prev = -1
for i in range(n):
    if a[i] == m:
        if prev != -1:
            ans = min(ans, i - prev)
        prev = i
print(ans)
