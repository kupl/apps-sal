n = int(input())
a = list(map(int, input().split()))
q = 1
for i in range(n - 1):
    if q == 1:
        a.remove(max(a))
    else:
        a.remove(min(a))
    q *= -1
print(a[0])
