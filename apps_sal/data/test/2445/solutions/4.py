def read():
    return map(int, input().split())


t = int(input())
for _ in range(t):
    n = int(input())
    print((n + 2) // 2)
