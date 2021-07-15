X, Y, A, B, C = [int(x) for x in input().split()]
p = sorted([int(x) for x in input().split()], reverse=True)[:X]
q = sorted([int(x) for x in input().split()], reverse=True)[:Y]
r = sorted([int(x) for x in input().split()], reverse=True)[:X + Y]

s = sorted(p + q + r, reverse=True)

ans = sum(s[:X + Y])

print(ans)
