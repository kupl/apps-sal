a = int(input())
for i in range(a):
    s = int(input())
    z = [i + 1 for i in range(s)]
    print(*z)
