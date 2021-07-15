n, x = list(map(int, input().split()))
distressed = 0

for i in range(n):
    f = input().split()

    if f[0] == '+':
        x += int(f[1])
    else:
        if x >= int(f[1]):
            x -= int(f[1])
        else:
            distressed += 1

print(x, distressed)

