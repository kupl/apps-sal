a, b, c = map(int, input().split())
k = int(input())

m = max(a, b, c)
re = sum([a, b, c]) - m
print(re + m * 2**(k))
