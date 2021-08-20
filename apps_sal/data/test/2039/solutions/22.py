a = int(input())
b = [int(i) for i in input().split()]
c = 0
for i in range(1, a - 1):
    if b[i - 1] < b[i] and b[i + 1] < b[i] or (b[i - 1] > b[i] and b[i + 1] > b[i]):
        c += 1
print(c)
