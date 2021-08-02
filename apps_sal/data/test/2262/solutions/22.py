_ = input()
s = set()

for x in input().split():
    x = list(set(tuple(x)))
    x.sort()
    s.add(tuple(x))

print(len(s))
