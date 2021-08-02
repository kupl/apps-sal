a, b, c, d = list(map(int, input().split()))
p = a / b; q = c / d;
r = (1 - p) * (1 - q);
print(p / (1 - r))
