n = int(input())
m = n + int(n / 2)
print(m)
out = ''
out1 = ''
j = 1
for i in range(2, n + 1, 2):
    out += str(i) + ' '
    out1 += str(j) + ' '
    j += 2
if n % 2 == 1:
    out1 += str(j) + ' '
print(out + out1 + out)
