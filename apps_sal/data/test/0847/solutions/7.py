(nn, xx) = input().split(' ')
n = int(nn)
x = int(xx)
a = input().split(' ')
s = 0
for i in range(n):
    s += int(a[i])
s = abs(s)
print((s + x - 1) // x)
