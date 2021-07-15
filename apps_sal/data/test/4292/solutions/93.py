n, k = map(int, input().split())
p = [int(i) for i in input().split()]

p = sorted(p)
print(sum(p[:k]))
