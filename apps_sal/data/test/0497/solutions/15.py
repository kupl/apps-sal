n = int(input())
colors = [int(x) for x in input().split()]
right = n - 1
left = 0
while colors[right] == colors[0]:
    right -= 1

while colors[left] == colors[-1]:
	left += 1

print(max(n - left - 1, right))
