import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b, k = [int(num) for num in lines.pop(0).split(" ")]
s1 = set(range(a, min(b, a + k)))
s2 = set(range(max(a, b - k + 1), b + 1))
lis = sorted(s1 | s2)
for i in lis:
    print(i)
