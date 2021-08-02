import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = int(lines.pop(0))
v_list = [int(num) for num in lines.pop(0).split(" ")]
c_list = [int(num) for num in lines.pop(0).split(" ")]
ans = 0
for v, c in zip(v_list, c_list):
    if v > c:
        ans += (v - c)
print(ans)
