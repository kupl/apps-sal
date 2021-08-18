A, B = list(map(int, input().split()))

ans = [['
A -= 1
B -= 1

for h in range(0, 100, 2):
    if A == 0:
        break
    for w in range(0, 100, 2):
        ans[h][w] = '.'
        A -= 1
        if A == 0:
            break

for h in range(0, 100, 2)[::-1]:
    if B == 0:
        break
    for w in range(0, 100, 2):
        ans[h][w] = '
        B -= 1
        if B == 0:
            break

print((100, 100))
for a in ans:
    print((''.join(a)))
