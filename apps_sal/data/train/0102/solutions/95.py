t = int(input())
for i in range(t):
    n = input()
    pos = (len(n) - 1) * 9
    x = 1
    while int(str(x) * len(n)) <= int(n):
        pos += 1
        x += 1
    print(pos)
