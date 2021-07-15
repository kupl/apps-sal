W, a, b = map(int, input().split())
f = lambda x:x if x > 0 else 0
print(f(abs(a-b)-W))
