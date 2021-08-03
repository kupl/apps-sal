n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
if l.count(l[0]) == l.count(l[n - 1]) == n / 2:
    print('YES')
    print(l[0], l[n - 1])
else:
    print("NO")
