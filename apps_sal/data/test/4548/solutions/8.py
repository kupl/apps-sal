import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, m, x = [int(num) for num in lines.pop(0).split(" ")]
a_list = [int(num) for num in lines.pop(0).split(" ")]

for i in range(m):
    if a_list[i] > x:
        break

ans = min(i, m - i)
print(ans)
