n = int(input())
l = list(map(int, input().split()))
max1 = max(l)
min1 = min(l)
ans = max1 - min1
print(ans, end=' ')
x = l.count(max1)
y = l.count(min1)
if(x == n):
    print(((n) * (n - 1)) // 2)
else:
    print(x * y)
