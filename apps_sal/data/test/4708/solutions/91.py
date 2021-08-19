n = int(input())
k = int(input())
x = int(input())
y = int(input())
ans = 0
if n > k:
    ans = k * x + (n - k) * y
else:
    ans = n * x
print(ans)
