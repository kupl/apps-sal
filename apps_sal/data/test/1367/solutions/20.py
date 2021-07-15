n = int(input())
s = sum([int(i) for i in input().split()])
print(n * (n + 1) // 2 - s)
