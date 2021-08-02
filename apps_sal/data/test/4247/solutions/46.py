a = int(input())
b = list(map(int, input().split()))
c = 0
for i in range(a - 2):
    if (b[i + 1] - b[i]) * (b[i + 2] - b[i + 1]) > 0:
        c = c + 1
print(c)
