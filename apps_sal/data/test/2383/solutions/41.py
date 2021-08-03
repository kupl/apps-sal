n = int(input())
a = [int(x) for x in input().split()]
c = 1
b = 0
for i in range(n):
    if a[i] == c:
        c += 1
    else:
        b += 1
if c == 1:
    res = -1
else:
    res = b
print(res)
