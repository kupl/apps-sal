n = int(input())
k = int(input())
x = int(input())
y = int(input())
s = 0
for i in range(1, n + 1, 1):
    if i <= k:
        s += x
    else:
        s += y
print(s)
