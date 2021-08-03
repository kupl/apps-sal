c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mn1, mn2 = 0, 0
for i in range(n):
    if(a[i] < c2 // c1 + 1):
        mn1 += c1 * a[i]
    else:
        mn1 += c2
for i in range(m):
    if(b[i] < c2 // c1 + 1):
        mn2 += c1 * b[i]
    else:
        mn2 += c2
print(min(c4, 2 * c3, mn1 + c3, mn2 + c3, mn1 + mn2))
