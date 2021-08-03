n = int(input())
line = list(map(int, input().split()))
line.sort()
print(line[n // 2] - line[n // 2 - 1])
