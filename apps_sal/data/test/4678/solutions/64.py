n = int(input())
a = list(map(int, input().split()))
ans = 0
h = a[0]
for i in range(n):
    ans += max(a[i],h) - a[i]
    h = max(a[i],h)
print(ans)
