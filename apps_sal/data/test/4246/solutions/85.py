f = list(input())
c = list(input())

print((sum(1 for _f, _c in zip(f, c) if _f == _c)))

