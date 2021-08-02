n, m = list(map(int, input().split()))
line = list(input())

for i in range(m):
    l, r, c1, c2 = input().split()
    l, r = int(l), int(r)
    for j in range(l - 1, r):
        el = line[j]
        if el == c1:
            line[j] = c2

print(''.join(line))
