n = int(input())
a = list(map(int, input().split()))
pre = a[0]
ok = True
for i in range(n):
    if pre > a[i]:
        ok = False
        break
    if a[i] > pre:
        a[i] -= 1
    pre = a[i]
print('Yes' if ok else 'No')
