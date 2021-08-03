n = int(input())
l = sorted([int(x) for x in input().split()])
print(sum(abs(a - (b + 1)) for a, b in zip(l, list(range(n)))))
