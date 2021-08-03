n = int(input())

a = list(map(int, input().split()))

res = []
seen = set()

for e in reversed(a):
    if e in seen:
        continue

    res.append(e)
    seen.add(e)

print(len(res))
print(' '.join(str(x) for x in reversed(res)))
