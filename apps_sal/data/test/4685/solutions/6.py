import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
num_list = [int(num) for num in lines.pop(0).split(" ")]
k, = [int(num) for num in lines.pop(0).split(" ")]

m = max(num_list)
ans = sum(num_list) - m + (m * (2 ** k))
print(ans)
