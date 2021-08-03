from sys import stdin, stdout


a, b = list(map(int, stdin.readline().rstrip().split()))
c, d = list(map(int, stdin.readline().rstrip().split()))

match = -1
set1 = set()
for i in range(a + b + max([b, d])):
    set1.add(b + i * a)

for i in range(a + b + max([b, d])):
    if d + i * c in set1:
        match = d + i * c
        break

print(match)
