n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = 0
for i in range(m):
    if a[i] >= (sum(a) / (4 * m)):
        total += 1
if total == m:
    print("Yes")
else:
    print("No")
