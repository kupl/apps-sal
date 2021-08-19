(s1, s2) = input().split()
a = []
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        a.append(s1[:i] + s2[:j])
a.sort()
print(a[0])
