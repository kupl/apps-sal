n = int(input())
rc = list(map(int, input().split(' ')))
bc = list(map(int, input().split(' ')))
(r, b) = (0, 0)
for i in range(n):
    if rc[i] == 1 and bc[i] != 1:
        r += 1
    if rc[i] != 1 and bc[i] == 1:
        b += 1
if r == 0:
    print(-1)
elif r > b:
    print(1)
else:
    print(int(b / r) + 1)
