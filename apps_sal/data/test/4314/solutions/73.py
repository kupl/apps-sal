(H, W) = map(int, input().split())
A = [input() for i in range(H)]
B = []
for row in A:
    if all((a == '.' for a in row)):
        continue
    B.append(row)
C = ['' for _ in range(len(B))]
for col in zip(*B):
    if all((a == '.' for a in col)):
        continue
    for (i, a) in enumerate(col):
        C[i] += a
for row in C:
    print(row)
