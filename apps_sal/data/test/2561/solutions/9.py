t = int(input())
for i in range(t):
    a = int(input())
    num = 1
    for j in range(30):
        if a & 1 << j:
            num *= 2
    print(num)
