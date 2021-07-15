3

c = list(map(int, input().split()))
print(min(sum(c) // 3, sum(c) - max(c)))
