n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
r = a.pop(0)
s = r
temp = 0
for i in range(n - 1):
    if abs(r - 2 * a[i]) < s:
        s = abs(r - 2 * a[i])
        temp = a[i]
print(r, temp)
