n = int(input())
d = []
for i in range(n):
    s, p = input().split()
    l = [s, -int(p), i + 1]
    d.append(l)
d.sort()
for x in d:
    print(x[2])
