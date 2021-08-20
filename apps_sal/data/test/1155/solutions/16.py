(n, m) = list(map(int, input().split()))
mn = 10 ** 9
for i in range(n):
    (a, b) = list(map(int, input().split()))
    mn = min(a / b * m, mn)
print(mn)
