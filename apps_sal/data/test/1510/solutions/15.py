(n, m) = list(map(int, input().split()))
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
b.reverse()
Res = 0
for i in range(min(n, m)):
    if a[i] < b[i]:
        Res += b[i] - a[i]
print(Res)
