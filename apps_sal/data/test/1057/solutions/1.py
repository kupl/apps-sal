n = int(input())
s = input()
a = s[0]
b = s[-1]
x = 0
while s[x] == a:
    x += 1
y = n - 1
while s[y] == b:
    y -= 1
x += 1
y = n - y
if a == b:
    print(x * y % 998244353)
else:
    print(x + y - 1)
