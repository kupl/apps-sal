(H, W) = list(map(int, input().split()))
A = [[p for p in input()] for _ in range(H)]
y = 0
while y < len(A):
    if all([p == '.' for p in A[y]]):
        del A[y]
    else:
        y += 1
x = 0
while x < len(A[0]):
    if all([row[x] == '.' for row in A]):
        for row in A:
            del row[x]
    else:
        x += 1
for row in A:
    print(''.join(row))
