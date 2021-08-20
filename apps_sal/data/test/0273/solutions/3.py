(a, b) = input().split()
l = []
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        l.append(a[:i] + b[:j])
l.sort()
print(l[0])
