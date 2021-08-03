import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
s = sum(int(c) for c in str(n))
if n % s == 0:
    print("Yes")
else:
    print("No")
