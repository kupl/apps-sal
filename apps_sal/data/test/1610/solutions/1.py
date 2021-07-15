import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
nums = [int(i) for i in my_file.readline().split(" ")]
n = nums[0]
k = nums[1]
p = list(range(1, n+1))
p = p[n-1:n-k-1:-1]+p[:n-k]
for i in p:
    print(i, end=' ')
