n, m = [int(x) for x in input().split()]
v = [0] * 101
for _ in range(n):
    curr = [int(x) for x in input().split()][1:]
    for x in curr:
        v[x] = 1

correct = True
for x in range(1, m + 1):
    if not v[x]:
        correct = False
        break

if correct:
    print("YES")
else:
    print("NO")
