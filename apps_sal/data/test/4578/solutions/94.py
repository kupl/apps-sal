n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
m.sort()
x = x - sum(m)
print(len(m) + x // m[0])
