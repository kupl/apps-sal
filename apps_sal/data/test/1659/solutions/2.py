(n, x) = map(int, input().split())
xx = 0
for _ in range(n):
    s = str(input()).split()
    if s[0] == '+':
        x += int(s[1])
    elif x >= int(s[1]):
        x -= int(s[1])
    else:
        xx += 1
print(x, xx)
