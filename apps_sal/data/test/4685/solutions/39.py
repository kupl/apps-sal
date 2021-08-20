(a, b, c) = list(map(int, input().split()))
k = int(input())
print(max([a, b, c]) * 2 ** k + sum([a, b, c]) - max([a, b, c]))
