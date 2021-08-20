n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[-1] - data[0] + 1 - n)
