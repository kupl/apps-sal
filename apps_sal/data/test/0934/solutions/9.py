x = input()
v = list(input().split())
c = [q[0] for q in v if q[0] == x[0]]
c.extend([q[1] for q in v if q[1] == x[1]])
print("YES" if len(c) > 0 else "NO")

