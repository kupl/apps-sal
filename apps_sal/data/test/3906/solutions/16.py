foo = []
(n, m) = input().split()
n = int(n)
m = int(m)
foo.append(1)
foo.append(1)
for i in range(max(n, m)):
    foo.append(foo[i + 1] + foo[i])
o = 2 * (foo[n] + foo[m] - 1)
print(o % 1000000007)
