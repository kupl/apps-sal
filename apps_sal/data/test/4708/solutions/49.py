n = int(input())
k = int(input())
x = int(input())
y = int(input())
ans = 0
if n >= k:
    ans += x * k
    n -= k
    ans += y * n
else:
    ans += x * n
print(ans)
