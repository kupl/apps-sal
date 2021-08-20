t = int(input())
x = [int(a) for a in input().split(' ')]
for i in range(0, t - 1):
    print(x[i] + x[i + 1], end=' ')
print(x[t - 1])
