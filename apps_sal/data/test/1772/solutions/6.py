def min(a, b):
    if a >= b:
        return b
    else:
        return a


b = 0
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(n):
    if a[i] % 2 == 0:
        b += 1
c = n - b
ans = min(b, c)
if b < c:
    ans += ((c - b) // 3)
print(ans)
