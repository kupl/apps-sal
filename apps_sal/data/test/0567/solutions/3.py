n = int(input())
v = [int(x) for x in input().split()]
Max = 0
for x in v:
	Max = max(Max, min(x - 1, 1000000 - x))
print(Max)

