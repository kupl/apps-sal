n = int(input())
p = [int(v) for v in input().split()]
p.sort()

a = sum(abs(pp - ii) for (ii, pp) in zip(list(range(1, n + 1, 2)), p))
b = sum(abs(pp - ii) for (ii, pp) in zip(list(range(2, n + 1, 2)), p))

print(min(a, b))

