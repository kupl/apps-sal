n = int(input())
a = list(map(int, input().split()))
d = set()
s = 0
for x in a:
    if x == 0 or x in d:
        continue
    s += 1
    d.add(x)
print(len(d))
