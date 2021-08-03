n = int(input())
k = int(input())
x = int(input())
y = int(input())

ans = min(n, k) * x
n -= min(n, k)

ans += n * y

print(ans)
