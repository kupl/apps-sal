a, b, c = list(map(int, input().split()))

sol = min(a, b, c)
sol += (a - sol) // 3 + (b - sol) // 3 + (c - sol) // 3

sol2 = min(a, b, c) - 1
sol2 += (a - sol2) // 3 + (b - sol2) // 3 + (c - sol2) // 3

sol3 = min(a, b, c) - 2
sol3 += (a - sol3) // 3 + (b - sol3) // 3 + (c - sol3) // 3

if min(a, b, c) == 0: sol1, sol2, sol3 = 0, 0, 0

print(max(sol, sol2, sol3))
