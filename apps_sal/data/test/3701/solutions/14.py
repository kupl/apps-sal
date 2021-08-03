n, x, y = list(map(int, input().strip().split(' ')))
s = input()
groups = 0
if s[0] == '0':
    groups += 1
for b in range(1, n):
    if s[b] == '0' and s[b - 1] == '1':
        groups += 1
if groups == 0:
    print(0)
else:
    print((groups - 1) * min(x, y) + y)
