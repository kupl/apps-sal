(x, y, a, b, c) = list(map(int, input().split()))
p = sorted(list(map(int, input().split())), reverse=True)[:x]
q = sorted(list(map(int, input().split())), reverse=True)[:y]
r = sorted(list(map(int, input().split())), reverse=True)[:x + y]
new = sorted(p + q + r, reverse=True)
print(sum(new[:x + y]))
