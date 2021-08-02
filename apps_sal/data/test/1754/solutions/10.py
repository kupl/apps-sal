n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in list(map(int, input().split())):
    m = 0
    for j in range(n):
        if b[i - 1] == b[j]:
            m = max(m, a[j])
    if m != a[i - 1]:
        res += 1
print(res)
