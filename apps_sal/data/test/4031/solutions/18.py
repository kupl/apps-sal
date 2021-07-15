n = int(input())
a = [None] * n
for i in range(n):
    a[i] = input()
a.sort(key=len)
f = True
for i in range(n - 1):
    if a[i] not in a[i + 1]:
        f = False
        break
if f:
    print("YES")
    for i in range(n):
        print(a[i])
else:
    print("NO")
