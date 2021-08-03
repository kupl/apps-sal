n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(sum(data[::2]) - sum(data[1::2]))
