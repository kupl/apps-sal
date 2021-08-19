t = {}
for i in range(int(input())):
    (a, b) = map(int, input().split())
    c = a * 60 + b
    t[c] = t.get(c, 0) + 1
print(max(t.values()))
