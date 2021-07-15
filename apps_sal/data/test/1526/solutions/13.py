a = list(map(int, input().split()))
ma = max(a)
d = ma*3 - sum(a)
print((d // 2 if d % 2 == 0 else d // 2 + 2))

