n = int(input())
a = list(map(int, input().split()))
b = list()
c = list()
if a == list(sorted(a)):
    print(0)
    return
for i in range(1, n):
    if a[i] < a[i - 1]:
        b.append(i)
ans = True
if len(b) == 1:
    for i in range(b[0], n):
        c.append(a[i])
    for i in range(b[0]):
        c.append(a[i])
    if c != list(sorted(a)):
        ans = False
if len(b) == 1 and ans:
    print(n - b[0])
else:
    print(-1)
