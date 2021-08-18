A, B = list(map(int, input().split()))

ans = [['
A -= 1
B -= 1

for h in range(0, 50, 2):
    for w in range(0, 100, 2):
        if A == 0:
            break
        ans[h][w] = '.'
        A -= 1

for h in range(0, 50, 2):
    for w in range(0, 100, 2):
        if B == 0:
            break
        ans[-(h + 1)][w] = '
        B -= 1

print((100, 100))
for a in ans:
    print((''.join(a)))
