import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

H1 = [0] * (10 ** 5)
H2 = [0] * (10 ** 5)
M = []

for i in range (0, n):
    x = a[i]
    h = ((x + 1234) ** 2) % 94999
    if H1[h] == 0:
        H1[h] = []
        H2[h] = []
    if x not in H1[h]:
        H1[h].append(x)
        H2[h].append(i)
        M.append(i)
    else:
        j = H2[h][H1[h].index(x)]
        while j < M[-1]:
            M.pop()

m = len(M) - 1
answer = 1
p = 2
while m > 0:
    if m % 2 == 1:
        answer = (answer * p) % 998244353
        m = m - 1
    p = (p * p) % 998244353
    m = m // 2

print(answer)
