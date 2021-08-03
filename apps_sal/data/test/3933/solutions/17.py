a = int(input())
b = list(map(int, input().split()))
n = 0
x = 0
if b[0] > b[1]:
    x = b[0] - b[1]
    for i in range(len(b) - 1):
        if b[i] - b[i + 1] != x:
            n = 1
    if n == 0:
        print(b[-1] - x)
    else:
        print(b[-1])
else:
    x = b[1] - b[0]
    for i in range(len(b) - 1):
        if b[i + 1] - b[i] != x:
            n = 1
    if n == 0:
        print(b[-1] + x)
    else:
        print(b[-1])
