n = int(input())
a = sorted(map(int, input().split()))
b = map(lambda x: abs(x), a)
ans = sum(a)
for i in range(1, n+n-1, 2):
    a[i] *= -1
    a[i-1] *= -1
    ans = max(ans, sum(a))
if n % 2 == 1:
    ans = max(ans, sum(b))
print (ans)
