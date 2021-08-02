import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
d, n = [int(num) for num in lines.pop(0).split(" ")]
if n == 100:
    n += 1
ans = (100 ** d) * n
print(ans)
