a = int(input())
b = [int(i) for i in input().split()]
for i in range(a):
    if i == 0:
        print(b[1] - b[0], b[a - 1] - b[0])
        continue
    if i == a - 1:
        print(b[a - 1] - b[a - 2], b[a - 1] - b[0])
    else:
        print(min(b[i + 1] - b[i], b[i] - b[i - 1]), max(b[i] - b[0], b[a - 1] - b[i]))
