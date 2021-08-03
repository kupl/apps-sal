n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i])
b.sort()
c = 0
for i in range(n):
    if a[i] != b[i]:
        c = c + 1
if c <= 2:
    print("YES")
else:
    print("NO")
