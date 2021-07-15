n, s, t = (int(x) for x in input().split())
p = [0] + [int(x) for x in input().split()]
val = 0
while s > 0 and s != t:
    nxt = p[s]
    p[s] = 0
    s = nxt
    val += 1
print(val if s else -1)
