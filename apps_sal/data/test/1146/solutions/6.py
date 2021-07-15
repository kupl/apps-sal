n, m = map(int, input().split())
s = set()
for i in range(n):
    a = list(map(int, input().split()))
    a = a[1:]
    s |= set(a)
if len(s) == m:
    print("YES")
else:
    print("NO")
