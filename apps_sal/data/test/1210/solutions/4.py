(n, p) = [int(i) for i in input().split()]
s = []
q = [(0, 0)] * n
for i in range(n):
    (l, r) = [int(i) for i in input().split()]
    s.append((l, r))
for i in range(n):
    q[i] = ((s[i][1] - s[i][1] % p - (s[i][0] + p - 1) // p * p) // p + 1, s[i][1] - s[i][0] + 1)
sm = 0
for i in range(n):
    sm += (1 - (q[i - 1][1] - q[i - 1][0]) / q[i - 1][1] * ((q[i][1] - q[i][0]) / q[i][1])) * 2000
print(sm)
