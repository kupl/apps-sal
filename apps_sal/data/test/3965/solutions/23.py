n = int(input())
a = list(map(int, input().split()))
f = True
for i in range(n):
    s = input()
    count = 0
    count = s.count('e')
    count += s.count('y')
    count += s.count('u')
    count += s.count('i')
    count += s.count('o')
    count += s.count('a')
    if count != a[i]:
        f = False
if f:
    print("YES")
else:
    print("NO")

