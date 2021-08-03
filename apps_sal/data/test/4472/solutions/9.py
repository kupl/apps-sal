n = int(input())
a = input()
b = input()
o = 0
for i in range(n // 2):
    if b[i] == b[n - 1 - i]:
        o += int(a[i] != a[n - 1 - i])
    else:
        o += 2 - len(set([a[i], a[n - 1 - i]]) & set([b[i], b[n - 1 - i]]))
if n % 2:
    o += int(a[n // 2] != b[n // 2])
print(o)
