from sys import *
m = int(input())
q = [0] * (m + 1)
c = 1
for i in range(m, 1, -1):
    w = m // i * pow(m, 1000000007 - 2, 1000000007)
    q[i] = w * pow(1 - w, 1000000007 - 2, 1000000007) % 1000000007
    for j in range(2 * i, m + 1, i):
        q[i] = (q[i] - q[j]) % 1000000007
    c = c + q[i]
print(c % 1000000007)
