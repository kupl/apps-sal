(n, m) = input().split()
(n, m) = (int(n), int(m))
s = input()
t = input()
min_c = 10 ** 4
min_pos = []
for i in range(m - n + 1):
    c = 0
    pos = []
    for j in range(n):
        if s[j] != t[i + j]:
            c += 1
            pos.append(j + 1)
    if c < min_c:
        min_c = c
        min_pos = pos[:]
print(min_c)
for i in range(len(min_pos) - 1):
    print(min_pos[i], end=' ')
if len(min_pos) > 0:
    print(min_pos[-1])
