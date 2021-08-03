n, m, x = map(int, input().split())
a = list(map(int, input().split()))
root0 = 0
rootn = 0
for i in range(1, x):
    if i in a:
        root0 += 1
for i in range(x + 1, n + 1):
    if i in a:
        rootn += 1
print(min(root0, rootn))
