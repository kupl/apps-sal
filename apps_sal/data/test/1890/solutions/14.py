(t, k) = (input(), int(input()))
(n, d) = (len(t), 1000000007)
p = (pow(2, k * n, d) - 1) * pow(pow(2, n, d) - 1, d - 2, d) % d
print(p * sum((pow(2, i, d) for i in range(n) if t[i] in '05')) % d)
