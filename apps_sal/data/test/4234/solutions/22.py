n = int(input())
a = input()

ans = 0
x = True
b = []
for i in range(n - 1):
    if x:
        if a[i] == a[i + 1]:
            b.append(i)  # +ans)
            ans += 1
            x = not x
    x = not x

if (n - ans) % 2:
    b.append(n - 1)
    ans += 1

# print(b)
print(ans)
b = set(b)
for i in range(n):
    if i not in b:
        print(a[i], end='')
