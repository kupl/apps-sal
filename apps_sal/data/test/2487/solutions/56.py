I, J, R = input, int, range; n = J(I()); A = sum(i * (n - i + 1)for i in R(1, n + 1))
for i in R(n - 1): u, v = map(J, I().split()); A -= min(u, v) * (n - max(u, v) + 1)
print(A)
