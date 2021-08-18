import sys
my_file = sys.stdin
my_file.readline()
nums = [int(i) for i in my_file.readline().split(" ")]
speaking = 0
for i in nums:
    if i > 0:
        if nums.count(i) == 2:
            speaking += 1
        elif nums.count(i) > 2:
            speaking = -1
            break
if speaking > 0:
    print(int(speaking / 2))
else:
    print(speaking)
