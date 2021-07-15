inf = float("inf")
points = [
	[inf, 3, 4],
	[3, inf, inf],
	[4, inf, inf]
]

tot = 0
n = int(input())
nums = [*map(int, input().split())]
for i in range(1, n):
	tot += points[nums[i - 1] - 1][nums[i] - 1]
	if i > 1 and (nums[i - 2], nums[i - 1], nums[i]) == (3, 1, 2):
		tot -= 1
if tot == inf:
	print("Infinite")
else:
	print("Finite")
	print(tot)
