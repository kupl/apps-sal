n = int(input())
a = []
for i in range(n):
    a.append(0)
for i in range(n - 1):
    b, c = input().split()
    a[int(b) - 1] += 1
    a[int(c) - 1] += 1
if2 = False
for i in range(n):
    if a[i] == 2:
        if2 = True
if if2:
    print("NO")
else:
    print("YES")
