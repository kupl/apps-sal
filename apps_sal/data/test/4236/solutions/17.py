[n, m] = [int(i) for i in input().split()]

arr = [0] * m

for i in range(n):
    [s, e] = [int(i) for i in input().split()]
    for i in range(s, e + 1):
        arr[i - 1] = 1

out = []
for i in range(m):
    if arr[i] == 0:
        out.append(i + 1)

print(len(out))
for i in out:
    print(i, end=" ")
print()
