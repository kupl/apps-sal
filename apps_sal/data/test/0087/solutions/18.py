(m, d) = list(map(int, input().split()))
l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m -= 1
t = l[m]
first_col = 8 - d
t -= first_col
c = 1
while t > 0:
    t -= 7
    c += 1
print(c)
