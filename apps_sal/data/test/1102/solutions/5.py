n, p = map(int, input().split())
p -= 1
a = list(map(int, input().split()))

res = a[p]
for i in range(1, len(a)):
    if p - i < 0 and p + i >= len(a):
        break

    if p - i < 0:
        res += a[p + i]
    elif p + i >= len(a):
        res += a[p - i]
    elif a[p + i] + a[p - i] == 2:
        res += 2
print(res)
