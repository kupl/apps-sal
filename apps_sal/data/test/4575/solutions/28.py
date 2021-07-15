import sys, math
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
d, x = [int(num) for num in lines.pop(0).split(" ")]
a_list = [int(line) for line in lines]
ans = x
for a in a_list:
    ans += math.ceil(d / a)
print(ans)

