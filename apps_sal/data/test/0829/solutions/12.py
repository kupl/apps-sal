n = int(input())
x = 0
y = 0
s = input()
for i in range(n):
    if s[i] == '0':
        x += 1
    else:
        y += 1
if x == y:
    print(2)
    print(s[:n - 1], s[n - 1])
else:
    print(1)
    print(s)
