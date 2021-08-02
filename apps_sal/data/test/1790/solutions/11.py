
n = int(input())
a = set(range(1, 101))
for i in range(n):
    a.intersection_update(set(map(int, input().split()[1:])))

for e in a:
    print(e, end=" ")
