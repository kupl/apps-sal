import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
s = lines.pop(0)

ans = 0
for i in range(n):
    intersection = set(s[:i]) & set(s[i:])
    num = len(intersection)
    if num > ans:
        ans = num
print(ans)
