(x, y, a, b, c) = map(int, input().split())
p = sorted([int(x) for x in input().split()])[::-1][:x]
q = sorted([int(x) for x in input().split()])[::-1][:y]
r = [int(x) for x in input().split()]
row = sorted(p + q + r)[::-1]
print(sum(row[:x + y]))
