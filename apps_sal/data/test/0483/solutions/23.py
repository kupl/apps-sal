n = int(input())
s = input()
pos = [int(i) for i in input().split()]
min = 10 ** 18
nosol = True
for i in range(1, n):
    if s[i - 1] == 'R' and s[i] == 'L':
        dist = pos[i] - pos[i - 1]
        if dist < min:
            min = dist
            nosol = False
if nosol:
    print(-1)
else:
    print(min >> 1)
