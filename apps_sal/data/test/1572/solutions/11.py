n = int(input())
l = [int(x) for x in input().split()]
x = 0
m = 0
for i in range(2, n):
    if l[i] == l[i - 1] + l[i - 2]:
        x += 1
    else:
        x += 2
        if x > m:
            m = x
        x = 0
x += 2
if x > m:
    m = x
    x = 0
if n <= 2:
    print(n)
else:
    print(m)
