n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
l, r = [list(i) for i in zip(*a)]
print(max(0, min(r) - max(l) + 1))
