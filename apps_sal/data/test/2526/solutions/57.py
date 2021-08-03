x, y, a, b, c = list(map(int, input().split()))
p = sorted(list(map(int, input().split())))[::-1]
q = sorted(list(map(int, input().split())))[::-1]
r = sorted(list(map(int, input().split())))[::-1]

u = sorted(p[:x] + q[:y] + r)[::-1]
print((sum(u[:x + y])))
