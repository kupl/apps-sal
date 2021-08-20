(n, k) = list(map(int, input().split()))
possible = []
for x in map(int, input().split()):
    if k % x == 0:
        possible.append(x)
print(min([k // x for x in possible]))
