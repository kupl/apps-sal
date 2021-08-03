n = int(input())
a = list(map(int, input().split()))
a.sort()
dup = 0
for i in range(0, n - 1):
    if a[i] == a[i + 1]:
        dup += 1
if dup % 2 == 1:
    dup += 1
print(n - dup)
