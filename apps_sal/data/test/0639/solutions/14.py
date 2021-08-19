(n, x) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [1] * 101
for i in a:
    b[i] = 0
c = sum(b[:x])
if x in a:
    c += 1
print(c)
