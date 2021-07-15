input()
a = list(map(int, input().split(' ')))
days = 0
resolves = set()
for i, b in enumerate(a):
    if not resolves:
        days += 1
    resolves.add(b)
    if i + 1 in resolves:
        resolves.remove(i + 1)
print(days)

