n = int(input())
(a, b) = (input(), input())
s = 0
for i in range(n):
    tmp = ord(a[i]) - ord(b[i])
    tmp %= 10
    if tmp > 5:
        s += 10 - tmp
    else:
        s += tmp
print(s)
