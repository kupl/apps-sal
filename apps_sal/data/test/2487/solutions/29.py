N = 0
a = 0

try:
    N = int(input())
    for i in range(N + 1):
        a += i * (i + 1) // 2
    for i in range(N - 1):
        line = input().split()
        u = min(int(line[0]), int(line[1])) - 1
        v = max(int(line[0]), int(line[1])) - 1
        a -= (u + 1) * (N - v)
except:
    pass

print(a)
