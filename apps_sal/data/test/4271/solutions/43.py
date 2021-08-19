n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
res = b[a[0] - 1]
for i in range(1, n):
    res += b[a[i] - 1]
    if a[i] - a[i - 1] == 1:
        res += c[a[i - 1] - 1]
print(res)
