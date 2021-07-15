n, m = map(int, input().split())
c = set(s.find("S") - s.find("G") for s in (input() for _ in range(n)))
print(-1 if any(a < 0 for a in c) else len(c))
