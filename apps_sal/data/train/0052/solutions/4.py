n = int(input())
a = [int(input()) for i in range(n)]
a.sort()
print(sum(map(lambda x, y: x * y, a, reversed(a))) % 10007)
