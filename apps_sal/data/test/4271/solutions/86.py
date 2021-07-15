n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
res = b[-1]
for i in range(n - 1):
    res += b[i]
    if a[i] + 1 == a[i + 1]:
        res += c[a[i] - 1]
print(res)
