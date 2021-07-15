f = []
for i in range(int(input())):
    f.append(tuple(int(x) for x in input().split()))
cur = 0
for t in sorted(f):
    cur = t[1] if cur <= t[1] else t[0]
print(cur)
