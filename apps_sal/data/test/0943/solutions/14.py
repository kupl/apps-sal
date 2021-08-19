(n, a) = (int(input()), list(map(int, input().split())))
o = [x for x in a if x % 2]
print(sum(a) - (min(o) if len(o) % 2 else 0))
