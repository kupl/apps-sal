a, b, c = map(int, input().split())
k = int(input())
print((2**k - 1) * max([a, b, c]) + sum([a, b, c]))
