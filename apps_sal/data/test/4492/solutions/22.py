N, x = map(int, input().split())
a = list(map(int, input().split()))
result = 0
if a[0] > x:
    result += a[0] - x
    a[0] = x
for i in range(N-1):
    if a[i] + a[i+1] > x:
        result += a[i] + a[i+1] - x
        a[i+1] = x - a[i]
print(result)
