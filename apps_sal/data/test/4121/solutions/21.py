n = int(input())
a = list(map(int,input().split()))
s = []
for i in range(n):
    a[i] = a[i] & 1
for i in range(n):
    if len(s) == 0 or s[-1] != a[i]:
        s.append(a[i])
    else:
        s.pop()
if len(s) <= 1:
    print("YES")
else:
    print("NO")

