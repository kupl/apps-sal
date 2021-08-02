n, m = list(map(int, input().split()))
print(((2**m) * (1900 * m + 100 * (n - m))))

# unit = 1900*m + 100*(n-m)
# p = 1 / (2**m)
# r = 1 - p
# ans / p = 1*1 + 2*r + 3*(r**2) + 4*(r**3) + ...
# ans * r / p = 1*r + 2*(r**2) + 3*(r**3) + 4*(r**4) + ...
# (ans / p) - (ans * r / p) = 1 + r + r**2 + r**3 + r**4 + ...
# (ans / p) * (1 - r) = 1 / (1 - r)
# ans = 1 / p = 2**m
# answer = ans * unit
