import sys

nums = [int(x) for x in sys.stdin.readline().split(" ")]
a = [int(x) for x in sys.stdin.readline().split(" ")]

t = nums[1]

curr = 1
while curr < t:
	curr += a[curr-1]
if curr == t:
	print("YES")
else:
	print("NO")
